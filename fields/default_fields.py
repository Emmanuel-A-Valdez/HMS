from rooms.models import Room, RoomType

# RoomType.objects.create(room_type="Standard King", price=49.49)
# RoomType.objects.create(room_type="Double Queen", price=49.49)
# RoomType.objects.create(room_type="Junior King Suite", price=84.99)
# RoomType.objects.create(room_type="Hospitality Suite", price=129.99)
# RoomType.objects.create(room_type="Bar King Suite", price=120.99)

for floor in range(1, 6):
    for room in range(40):
        Room.objects.create(
            room_type=RoomType.objects.get(pk=1),
            room_number=str(floor * 100 + room) + "A",
            room_floor=floor,
        )
        Room.objects.create(
            room_type=RoomType.objects.get(pk=2),
            room_number=str(floor * 100 + room) + "B",
            room_floor=floor,
        )

    for room in range(40, 65):
        Room.objects.create(
            room_type=RoomType.objects.get(pk=3),
            room_number=str(floor * 100 + room),
            room_floor=floor,
        )

    for room in range(65, 80):
        Room.objects.create(
            room_type=RoomType.objects.get(pk=4),
            room_number=str(floor * 100 + room),
            room_floor=floor,
        )

    for room in range(80, 100):
        Room.objects.create(
            room_type=RoomType.objects.get(pk=5),
            room_number=str(floor * 100 + room),
            room_floor=floor,
        )
