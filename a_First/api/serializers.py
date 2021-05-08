from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)

    # this method automatically invoke when you save data
    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    # this method automatically invoke when you update data
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.city = validated_data.get("city", instance.city)
        instance.phone = validated_data.get("name", instance.phone)
        instance.save()
        return instance

    # you can implement validation hare reference-> https://testdriven.io/blog/drf-serializers/


# if you use serializers.ModalSerializer you need to write less code
# if you use serializers.ModalSerializer you don't need to write create and update methods
# you can use serializers.Serializer or serializers.ModalSerializer


# Example:
'''
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', 'city', 'phone']
        # or
        # fields = '__all__' # for all field
        # or
        # exclude = ['age', 'city']  # all field except "age" and "city"

        # Comment: you don't need to write create and update methods

        # Comment: validation (optional)
        # read_only_field = ['age', 'city'] # you can only read those fields

        # Comment: you can implement validation hare reference-> https://testdriven.io/blog/drf-serializers/
'''