from SocialTravel.models import Post

a = ["a","b","c","d"]

for _ in range(0,4):
    Post(carousel_caption_title=a[_], 
    carousel_caption_description="Un carousel descript",
    heading="Mi viaje",
    description="una description",
    un_campo= ""
    ).save()
