from django.contrib.auth import get_user_model, password_validation
from User.api.serializers import SignupSerializer, LoginSerializer, PasswordChangeSerializer, ProfileDetailSerializer, ProfileUpdateSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError, PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView




User = get_user_model()

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) # ---> getting the data from serializers class
        if serializer.is_valid(raise_exception = True):
            # --- validating serializers.py data ---
            first_name = serializer.validated_data['first_name'] 
            last_name = serializer.validated_data['last_name'] 
            email = serializer.validated_data['email'] 
            password = serializer.validated_data['password']
            print(password)
            user_type = serializer.validated_data['user_type']
            temporary_address = serializer.validated_data['temporary_address']
            permanent_address = serializer.validated_data['permanent_address']
            phone = serializer.validated_data['phone']
            date_of_birth = serializer.validated_data['date_of_birth']
            user = User.objects.create(first_name=first_name, last_name = last_name, email=email, user_type=user_type, temporary_address=temporary_address, permanent_address=permanent_address, date_of_birth=date_of_birth)
            user.set_password(password)
            user.is_verified = True
            user.save()
            return Response(serializer.data)

class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
            except User.DoesNotExist:
                raise NotFound({"email": "User with the provided email does not exist."})  # exception message
            if not user.check_password(serializer.validated_data['password']):
                raise ValidationError({'password': "Incorrect password"})
            if not (user.is_active or user.is_verified):
                raise ValidationError({'email': "User not activated or is unverified"})
            token = RefreshToken.for_user(user)  # method to generating access and refresh token for users
            print(dir(token))
            return Response({
                'refresh': str(token),
                'access': str(token.access_token)
            })

class PasswordChangeAPIView(APIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data,
                                              context={
                                                  'user': request.user
                                              })  # getting data from serializers and passing logged in user data to serializers using context
        if serializer.is_valid(raise_exception=True):  # exception raise if anything goes wrong
            password = serializer.validated_data['new_password']
            user = request.user
            user.set_password(password)  # setting up the new_password for user
            user.save()
            return Response({"success": "Password changed successfully"})

class ProfileView(RetrieveAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):  # overriding default behaviour of get_object that is used by retrieve API view
        return self.request.user

    # def retrieve(self, request, *args, **kwargs): # how retrieve api view is processing the data and giving response
    #     obj = self.get_object()
    #     serializer = self.serializer_class(obj)
    #     return Response(serializer.data)

class ProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user # self.request.user always returns logged in user

class ProfileDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


