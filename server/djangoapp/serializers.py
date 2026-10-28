from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CarMake, CarModel, Dealer, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['id', 'name', 'description']


class CarModelSerializer(serializers.ModelSerializer):
    make_name = serializers.CharField(source='make.name', read_only=True)
    
    class Meta:
        model = CarModel
        fields = ['id', 'make', 'make_name', 'name', 'car_type', 'year']


class DealerSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='name', read_only=True)
    short_name = serializers.SerializerMethodField()
    zip = serializers.CharField(source='zip_code', read_only=True)
    lat = serializers.SerializerMethodField()
    long = serializers.SerializerMethodField()

    class Meta:
        model = Dealer
        fields = ['id', 'city', 'state', 'address', 'zip', 'lat', 'long',
                  'short_name', 'full_name', 'name', 'zip_code',
                  'phone', 'email', 'website', 'short_desc', 'full_desc', 'review_count']

    def get_review_count(self, obj):
        return obj.reviews.count()

    def get_short_name(self, obj):
        coords = {1: 'Best Motors', 2: 'Elite Auto', 3: 'Quality Cars', 4: 'Premier Auto'}
        return coords.get(obj.id, obj.name.split()[0] if obj.name else '')

    def get_lat(self, obj):
        coords = {1: 42.3601, 2: 39.0997, 3: 37.6872, 4: 37.7749}
        return coords.get(obj.id, 40.0)

    def get_long(self, obj):
        coords = {1: -71.0589, 2: -94.5786, 3: -97.3301, 4: -122.4194}
        return coords.get(obj.id, -80.0)


class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.username', read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'dealer', 'dealer_name', 'customer', 'customer_name', 
                  'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year',
                  'review_text', 'sentiment', 'created_at', 'updated_at']
        read_only_fields = ['customer', 'sentiment', 'created_at', 'updated_at']
