from rest_framework import serializers
from django.core.mail import send_mail
from .models import CustomUser, VerificationCode

class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create_verification_code(self):
        email = self.validated_data['email']
        user, created = CustomUser.objects.get_or_create(email=email, username=email.split('@')[0])

        verification_code, created = VerificationCode.objects.get_or_create(user=user)
        verification_code.save()

        # Email yuborish
        send_mail(
            'Your Verification Code',
            f'Your verification code is: {verification_code.code}',
            'admin@example.com',
            [email],
            fail_silently=False,
        )
        return {'message': 'Verification code sent to email'}

class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        code = data.get('code')

        try:
            user = CustomUser.objects.get(email=email)
            verification = VerificationCode.objects.get(user=user, code=code)
        except (CustomUser.DoesNotExist, VerificationCode.DoesNotExist):
            raise serializers.ValidationError("Invalid verification code")

        user.is_verified = True
        user.set_password('defaultpassword')  # Foydalanuvchi keyin parolni o'zgartirishi mumkin
        user.save()
        verification.delete()

        return {'message': 'Account verified successfully'}
