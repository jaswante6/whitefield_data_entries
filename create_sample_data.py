import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_entry_project.settings')
django.setup()

from entry_app.models import PersonalInfo, BusinessAd

def create_sample_data():
    # Get existing business or create a new one
    business = PersonalInfo.objects.filter(profession__iexact='business').first()
    if not business:
        business = PersonalInfo.objects.create(
            name="Sample Business",
            profession="Business",
            area="Downtown",
            city="Mumbai",
            state="Maharashtra"
        )
        print(f"Created new business: {business.name}")
    else:
        print(f"Using existing business: {business.name}")

    # Create a sample business ad
    ad = BusinessAd.objects.create(
        business=business,
        headline="Special Discount on All Products!",
        description="We are offering amazing discounts on our entire product range. Visit our store today to get the best deals on premium quality items.",
        offers="50% off on all items this weekend only! Buy 2 get 1 free on selected products.",
        home_delivery=True,
        free_delivery=True,
        delivery_areas="Mumbai, Thane, Navi Mumbai",
        keywords="discount, sale, offers, free delivery, premium products"
    )
    print(f"Created business ad: {ad.headline}")

    # Create another sample business ad
    ad2 = BusinessAd.objects.create(
        business=business,
        headline="New Products Arrival",
        description="We have just received a fresh stock of latest products. Be the first to check out our new collection.",
        offers="Get 10% discount on new arrivals when you show this ad.",
        home_delivery=True,
        free_delivery=False,
        delivery_areas="Within 10km of our store",
        keywords="new arrival, latest products, collection, fashion"
    )
    print(f"Created business ad: {ad2.headline}")

if __name__ == "__main__":
    create_sample_data() 