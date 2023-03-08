from SocialTravel.models import Post
for _ in range(0,5):
    Post(carousel_caption_title="Un Carousel Title", 
    carousel_caption_description="Un carousel descript",
    heading="Mi viaje",
    description="una description",
    un_campo= ""
    ).save()
