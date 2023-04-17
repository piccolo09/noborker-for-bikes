from devutils.models import AbstractModel

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class VehicleCategory(models.Model):
    name = models.CharField(
        _("Vehicle Cateogry Name"),
        max_length=255,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Bike Categories"

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class VehicleManufacturer(models.Model):
    name = models.CharField(
        _("Vehicle Manufacturer Name"),
        max_length=255,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Vehicle Manufacturers"

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class VehicleModel(models.Model):
    name = models.CharField(
        _("Model Name"),
        max_length=255,
    )
    brand = models.ForeignKey(VehicleManufacturer, on_delete=models.RESTRICT, related_name="models")
    category = models.ForeignKey(
        VehicleCategory, on_delete=models.RESTRICT, related_name="models", blank=True, null=True
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Vehicle Model"
        verbose_name_plural = "Vehicle Models"

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.brand.slug}-{self.name}")
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class VehicleVariant(models.Model):
    name = models.CharField(
        _("Variant Name"),
        max_length=255,
    )
    model = models.ForeignKey(VehicleModel, on_delete=models.RESTRICT, related_name="variants")
    slug = models.SlugField(unique=True)
    bike_description = models.TextField(_("About"), blank=True, null=True)
    fuel_economy = models.FloatField(_("Mileage Km/L"), blank=True, null=True)
    fuel_tank_capacity = models.FloatField(_("Fuel Tank Capacity (in Liters)"), blank=True, null=True)
    seat_height = models.IntegerField(_("Seat Height (in mm)"), blank=True, null=True)

    class Meta:
        verbose_name = "Vehicle Variant"
        verbose_name_plural = "Vehicle Variants"

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.model.slug}-{self.name}")
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class VehicleListing(AbstractModel):
    name = models.CharField(
        _("Variant Name"),
        max_length=255,
    )
    variant = models.ForeignKey(VehicleVariant, on_delete=models.RESTRICT, related_name="listings")
    slug = models.SlugField(unique=True)
    registration_date = models.DateField(_("Registration date"))
    available_after = models.DateField(_("Availibility Date"), auto_now_add=True)
    last_service_date = models.DateField(_("Last Serviced at"), auto_now_add=True)
    day_rent = models.DecimalField(_("Rent Per Day"), blank=True, null=True, max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Vehicle Listing"
        verbose_name_plural = "Vehicle Listings"

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.variant.slug}-{self.name}")
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"
