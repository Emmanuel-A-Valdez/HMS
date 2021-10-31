from rooms.models import Room, RoomType
from bookings.models import Booking
from rooms.models import Room
from django.db.models import Q


def get_available_room(r_type, checkin, checkout):

    rm_type = RoomType.objects.filter(room_type=r_type)[0]
    qs = (
        Room.objects.select_related("room_type")
        .filter(room_type=rm_type)
        .exclude(
            Q(booking__check_in__gte=checkin, booking__check_out__lte=checkout)
            | Q(booking__check_in__lte=checkin, booking__check_out__gte=checkin)
            | Q(booking__check_in__lte=checkout, booking__check_out__gte=checkout)
        )
    )
    # print(qs)
    # print("**", qs[0].pk)

    return f"{qs[0].room_number}"
