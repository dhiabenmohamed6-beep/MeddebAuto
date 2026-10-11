import uuid
from django.db import models


class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('BROUILLON', 'Brouillon'),
        ('PUBLIÉ', 'Publié'),
        ('RÉSERVÉ', 'Réservé'),
        ('VENDU', 'Vendu'),
        ('ARCHIVÉ', 'Archivé'),
    ]
    CONDITION_CHOICES = [
        ('Neuf', 'Neuf'),
        ('Occasion', 'Occasion'),
        ('Collection', 'Collection'),
        ('Démonstration', 'Démonstration'),
    ]
    FUEL_CHOICES = [
        ('Essence', 'Essence'),
        ('Diesel', 'Diesel'),
        ('Hybride', 'Hybride'),
        ('Électrique', 'Électrique'),
        ('GPL', 'GPL'),
        ('Autre', 'Autre'),
    ]
    TRANSMISSION_CHOICES = [
        ('Automatique', 'Automatique'),
        ('Manuelle', 'Manuelle'),
        ('Séquentielle', 'Séquentielle'),
    ]
    BODY_CHOICES = [
        ('SUV', 'SUV'),
        ('Berline', 'Berline'),
        ('Coupé', 'Coupé'),
        ('Cabriolet', 'Cabriolet'),
        ('Break', 'Break'),
        ('Sportive', 'Sportive'),
        ('Citadine', 'Citadine'),
        ('Monospace', 'Monospace'),
        ('Utilitaire', 'Utilitaire'),
    ]
    BADGE_CHOICES = [
        ('NOUVEAUTÉ', 'Nouveauté'),
        ('PROMOTION', 'Promotion'),
        ('COUP DE CŒUR', 'Coup de Cœur'),
        ('EXCLUSIVITÉ', 'Exclusivité'),
        ('', 'Aucun'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BROUILLON')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    old_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, default='EUR')
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    body_type = models.CharField(max_length=20, choices=BODY_CHOICES)
    horsepower = models.IntegerField(null=True, blank=True)
    engine_size = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    cylinders = models.IntegerField(null=True, blank=True)
    doors = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    owners_count = models.IntegerField(null=True, blank=True)
    first_registration = models.CharField(max_length=20, blank=True, default='')
    country_origin = models.CharField(max_length=100, blank=True, default='')
    exterior_color = models.CharField(max_length=50, blank=True, default='')
    interior_color = models.CharField(max_length=50, blank=True, default='')
    upholstery = models.CharField(max_length=50, blank=True, default='')
    warranty = models.BooleanField(default=False)
    warranty_months = models.IntegerField(null=True, blank=True)
    service_history = models.BooleanField(default=False)
    accident_history = models.BooleanField(default=False)
    imported = models.BooleanField(default=False)
    title = models.CharField(max_length=200, blank=True, default='')
    short_description = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    featured = models.BooleanField(default=False)
    badge = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True, default='')
    primary_image = models.URLField(blank=True, default='')
    images = models.JSONField(default=list, blank=True)
    equipment = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['brand']),
            models.Index(fields=['model']),
            models.Index(fields=['status']),
            models.Index(fields=['featured']),
            models.Index(fields=['year']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.reference})"


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name