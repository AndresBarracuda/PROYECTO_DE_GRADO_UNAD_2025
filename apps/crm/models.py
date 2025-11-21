from datetime import date, timedelta
from django.db import models
from ckeditor.fields import RichTextField


def date_today(date_output=False, **kwargs):
    try:
        date_after = date.today() + timedelta(days=int(kwargs["days_after"]))

        if date_output:
            return date_after

        else:
            return date_after.strftime("%Y-%m-%d")

    except:
        if date_output:
            return date.today()

        else:
            return date.today().strftime("%Y-%m-%d")


##############
## Settings ##
##############


#   ======================   #
#   Table name: StatusCode   #
#   ======================   #
class StatusCode(models.Model):
    status_code_id = models.AutoField(
        verbose_name="Primary key of the status code (A.I)",
        primary_key=True,
    )

    status_code_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    status_code_registration_date = models.DateTimeField(
        verbose_name="Status code registration date",
        auto_now=False,
        auto_now_add=True,
    )

    status_code_update_date = models.DateTimeField(
        verbose_name="Status code update date",
        auto_now=True,
    )

    status_code_code = models.PositiveIntegerField(
        verbose_name="Status code",
        blank=False,
        null=False,
        unique=True,
        editable=False,
        default=101,
    )

    status_code_name = models.CharField(
        verbose_name="Description of the status code",
        max_length=100,
        blank=False,
        null=False,
    )

    status_code_spanish_name = models.CharField(
        verbose_name="Description of the status code (Spanish)",
        max_length=100,
        blank=False,
        null=False,
    )

    status_code_status = models.BooleanField(
        verbose_name="Status of the status code for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Status code"
        verbose_name_plural = "Status codes"
        ordering = [
            "status_code_name",
        ]

    def __str__(self):
        return "{}".format(
            self.status_code_name,
        )


#   ==========================   #
#   Table name: CustomSettings   #
#   ==========================   #
class CustomSettings(models.Model):
    custom_settings_id = models.AutoField(
        verbose_name="Primary key of the custom settings",
        primary_key=True,
    )

    custom_settings_mailing_api_key = models.TextField(
        verbose_name="Mailing API key",
        blank=True,
        null=True,
        editable=False,
    )

    custom_settings_crab_api_key = models.TextField(
        verbose_name="Crab API key",
        blank=True,
        null=True,
        editable=True,
    )

    custom_settings_barracuda_notifications_key = models.TextField(
        verbose_name="Barracuda notifications key",
        blank=True,
        null=True,
        editable=False,
    )

    custom_settings_customer_notifications_key = models.TextField(
        verbose_name="Customer notifications key",
        blank=True,
        null=True,
        editable=False,
    )

    custom_settings_status_code = models.OneToOneField(
        verbose_name="Response status code",
        to=StatusCode,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    custom_settings_shopping_center_name = models.CharField(
        verbose_name="Name of the shopping center",
        max_length=50,
        blank=False,
        null=False,
    )

    custom_settings_company_name = models.CharField(
        verbose_name="Company name",
        max_length=100,
        blank=False,
        null=False,
    )

    custom_settings_nit = models.CharField(
        verbose_name="Company NIT number",
        max_length=20,
        blank=False,
        null=False,
    )

    custom_settings_domain = models.URLField(
        verbose_name="Web site",
        blank=False,
        null=False,
        default="https://www.unad.edu.co/",
    )

    custom_settings_data_processing_authorization = RichTextField(
        verbose_name="Data processing authorization",
        blank=False,
        null=False,
    )

    custom_settings_vertical_imagotypical_image = models.ImageField(
        verbose_name="Vertical imagotypical image",
        upload_to="customer_images/",
        blank=False,
        null=False,
    )

    custom_settings_horizontal_imagotypical_image = models.ImageField(
        verbose_name="Horizontal imagotypical image",
        upload_to="customer_images/",
        blank=False,
        null=False,
    )

    custom_settings_isotypical_image = models.ImageField(
        verbose_name="Isotypical image",
        upload_to="customer_images/",
        blank=False,
        null=False,
    )

    custom_settings_mailing_enabled = models.BooleanField(
        verbose_name="Mailing enabled",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_wacom = models.BooleanField(
        verbose_name="Wacom enabled",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_blood_type_required = models.BooleanField(
        verbose_name="Blood type required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_landline_number_required = models.BooleanField(
        verbose_name="Landline number required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_residence_address_required = models.BooleanField(
        verbose_name="Residence address",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_neighborhood_required = models.BooleanField(
        verbose_name="Neighborhood required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_social_class_required = models.BooleanField(
        verbose_name="Social class required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_marital_status_required = models.BooleanField(
        verbose_name="Marital status required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_occupation_required = models.BooleanField(
        verbose_name="Occupation required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_health_plan_required = models.BooleanField(
        verbose_name="Health plan required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_emergency_contact_required = models.BooleanField(
        verbose_name="Emergency contact required",
        blank=False,
        null=False,
        default=False,
    )

    custom_settings_status = models.BooleanField(
        verbose_name="Status of the custom settings",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Custom setting"
        verbose_name_plural = "Custom settings"
        ordering = [
            "custom_settings_id",
        ]

    def __str__(self):
        return "{}".format(
            self.custom_settings_shopping_center_name,
        )


class CommercialPremiseCategory(models.Model):
    commercial_category_id = models.AutoField(
        verbose_name="Primary key of the commercial premise category (A.I)",
        primary_key=True,
    )

    commercial_category_name = models.CharField(
        verbose_name="Name of the commercial premise category",
        max_length=100,
        blank=False,
        null=False,
    )

    commercial_category_status = models.BooleanField(
        verbose_name="Status of the commercial premise category for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Commercial premise category"
        verbose_name_plural = "Commercial premise categories"
        ordering = [
            "commercial_category_id",
        ]

    def __str__(self):
        return "{}".format(
            self.commercial_category_name,
        )

#   =============================   #
#   Table name: CommercialPremise   #
#   =============================   #
class CommercialPremise(models.Model):
    commercial_premise_id = models.AutoField(
        verbose_name="Primary key of the commercial premise (A.I)",
        primary_key=True,
    )

    commercial_premise_invoices = models.PositiveIntegerField(
        verbose_name="Commercial premise invoices",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    commercial_premise_name = models.CharField(
        verbose_name="Name of the commercial premise",
        max_length=100,
        blank=False,
        null=False,
    )

    commercial_premise_nomenclature = models.CharField(
        verbose_name="Nomenclature of the commercial premise",
        max_length=25,
        blank=False,
        null=False,
    )

    commercial_premise_category = models.ForeignKey(
        verbose_name="Category of the commercial premise",
        to=CommercialPremiseCategory,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    commercial_premise_anchor = models.BooleanField(
        verbose_name="Is the commercial premises an anchor",
        blank=False,
        null=False,
        default=False,
    )

    commercial_premise_purchase = models.BigIntegerField(
        verbose_name="Accumulated purchase",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    commercial_premise_status = models.BooleanField(
        verbose_name="Status of the commercial premise for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Commercial premise"
        verbose_name_plural = "Commercial premises"
        ordering = [
            "-commercial_premise_purchase",
        ]

    def __str__(self):
        return "{} | {} | {}".format(
            self.commercial_premise_name,
            self.commercial_premise_nomenclature,
            self.commercial_premise_category,
        )


#   ========================   #
#   Table name: ExceptionLog   #
#   ========================   #
class ExceptionLog(models.Model):
    exception_log_id = models.AutoField(
        verbose_name="Primary key of the exception log (A.I)",
        primary_key=True,
    )

    exception_log_registration_date = models.DateTimeField(
        verbose_name="Exception log registration date",
        auto_now=False,
        auto_now_add=True,
    )

    exception_log_description = models.TextField(
        verbose_name="Description of exception",
        blank=True,
        null=True,
    )

    exception_log_custom_settings = models.ForeignKey(
        verbose_name="Custom settings",
        to=CustomSettings,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    exception_log_status_code = models.ForeignKey(
        verbose_name="Status code",
        to=StatusCode,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Exception"
        verbose_name_plural = "Exceptions"
        ordering = [
            "-exception_log_id",
        ]

    def __str__(self):
        return "{}".format(
            self.exception_log_registration_date,
        )


####################
## Customers data ##
####################


#   =========================   #
#   Table name: TypeOfVehicle   #
#   =========================   #
class TypeOfVehicle(models.Model):
    type_vehicle_id = models.AutoField(
        verbose_name="Primary key of the vehicle type (A.I)",
        primary_key=True,
    )

    type_vehicle_name = models.CharField(
        verbose_name="Vehicle type name",
        max_length=50,
        blank=False,
        null=False,
    )

    type_vehicle_status = models.BooleanField(
        verbose_name="Status of the vehicle type for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Type of vehicle"
        verbose_name_plural = "Types of vehicle"
        ordering = [
            "type_vehicle_id",
        ]

    def __str__(self):
        return "{}".format(
            self.type_vehicle_name,
        )


#   =========================   #
#   Table name: MeansOfTransport   #
#   =========================   #
class MeansOfTransport(models.Model):
    means_of_transport_id = models.AutoField(
        verbose_name="Primary key of the means of transport (A.I)",
        primary_key=True,
    )

    means_of_transport_name = models.CharField(
        verbose_name="Vehicle type name",
        max_length=50,
        blank=False,
        null=False,
    )

    means_of_transport_status = models.BooleanField(
        verbose_name="Status of the means of transport for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Mean of transport"
        verbose_name_plural = "Means of transport"
        ordering = [
            "means_of_transport_id",
        ]

    def __str__(self):
        return "{}".format(
            self.means_of_transport_name,
        )


#   ======================   #
#   Table name: TypeOfPets   #
#   ======================   #
class TypeOfPets(models.Model):
    type_pet_id = models.AutoField(
        verbose_name="Primary key of the type of pet (A.I)",
        primary_key=True,
    )

    type_pet_name = models.CharField(
        verbose_name="Name of pet type",
        max_length=50,
        blank=False,
        null=False,
    )

    type_pet_status = models.BooleanField(
        verbose_name="Pet type status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Type of pets"
        verbose_name_plural = "Types of pets"
        ordering = [
            "type_pet_id",
        ]

    def __str__(self):
        return "{}".format(
            self.type_pet_name,
        )


#   ===================   #
#   Table name: Kinship   #
#   ===================   #
class Kinship(models.Model):
    kinship_id = models.AutoField(
        verbose_name="Kinship primary key (A.I)",
        primary_key=True,
    )

    kinship_name = models.CharField(
        verbose_name="Kinship name",
        max_length=50,
        blank=False,
        null=False,
    )

    kinship_status = models.BooleanField(
        verbose_name="Kinship status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Kinship"
        verbose_name_plural = "Kinships"
        ordering = [
            "kinship_id",
        ]

    def __str__(self):
        return "{}".format(
            self.kinship_name,
        )


#   ======================   #
#   Table name: HealthPlan   #
#   ======================   #
class HealthPlan(models.Model):
    health_plan_id = models.AutoField(
        verbose_name="Primary key of the Health plan (A.I)", primary_key=True
    )

    health_plan_name = models.CharField(
        verbose_name="Name of health plan",
        max_length=50,
        blank=False,
        null=False,
    )

    health_plan_status = models.BooleanField(
        verbose_name="Status of the health plan for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Health plan"
        verbose_name_plural = "Health plans"
        ordering = [
            "health_plan_id",
        ]

    def __str__(self):
        return "{}".format(
            self.health_plan_name,
        )


#   =========================   #
#   Table name: MaritalStatus   #
#   =========================   #
class MaritalStatus(models.Model):
    marital_status_id = models.AutoField(
        verbose_name="Primary key of the marital status (A.I)",
        primary_key=True,
    )

    marital_status_name = models.CharField(
        verbose_name="Name of marital status",
        max_length=50,
        blank=False,
        null=False,
    )

    marital_status_status = models.BooleanField(
        verbose_name="Status of the marital status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Marital status"
        verbose_name_plural = "Marital statuses"
        ordering = [
            "marital_status_id",
        ]

    def __str__(self):
        return "{}".format(
            self.marital_status_name,
        )


#   ======================   #
#   Table name: Department   #
#   ======================   #
class Department(models.Model):
    department_id = models.AutoField(
        verbose_name="Primary key of the department (A.I)",
        primary_key=True,
    )

    department_name = models.CharField(
        verbose_name="Name of the department",
        max_length=100,
        blank=False,
        null=False,
    )

    department_status = models.BooleanField(
        verbose_name="Status of the department for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = [
            "department_id",
        ]

    def __str__(self):
        return "{}".format(
            self.department_name,
        )


#   ================   #
#   Table name: City   #
#   ================   #
class City(models.Model):
    city_id = models.AutoField(
        verbose_name="Primary key of the city (A.I)",
        primary_key=True,
    )

    city_name = models.CharField(
        verbose_name="Name of the city",
        max_length=100,
        blank=False,
        null=False,
    )

    city_department = models.ForeignKey(
        verbose_name="Department of the city",
        to=Department,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    city_status = models.BooleanField(
        verbose_name="Status of the city for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = [
            "city_id",
        ]

    def __str__(self):
        return "{}".format(
            self.city_name,
        )


#   ==========================   #
#   Table name: PopulatedPlace   #
#   ==========================   #
class PopulatedPlace(models.Model):
    populated_place_id = models.AutoField(
        verbose_name="Primary key of the populated place (A.I)",
        primary_key=True,
    )

    populated_place_name = models.CharField(
        verbose_name="Name of the populated place",
        max_length=100,
        blank=False,
        null=False,
    )

    populated_place_city = models.ForeignKey(
        verbose_name="City of the populated place",
        to=City,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    populated_place_status = models.BooleanField(
        verbose_name="Status of the populated place for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Populated place"
        verbose_name_plural = "Populated places"
        ordering = [
            "populated_place_id",
        ]

    def __str__(self):
        return "{}".format(
            self.populated_place_name,
        )


#   ========================   #
#   Table name: Neighborhood   #
#   ========================   #
class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(
        verbose_name="Neighborhood primary key (A.I)",
        primary_key=True,
    )

    neighborhood_name = models.CharField(
        verbose_name="Name of the neighborhood",
        max_length=100,
        blank=False,
        null=False,
    )

    neighborhood_zonal_planning_unit = models.CharField(
        verbose_name="Neighborhood Zonal Planning Unit - ZPU",
        max_length=100,
        blank=False,
        null=False,
    )

    neighborhood_populated_place = models.ForeignKey(
        verbose_name="Populated place of the neighborhood",
        to=PopulatedPlace,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    neighborhood_social_class = models.PositiveSmallIntegerField(
        verbose_name="Neighborhood social class",
        blank=True,
        null=True,
    )

    neighborhood_status = models.BooleanField(
        verbose_name="Neighborhood status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Neighborhood"
        verbose_name_plural = "Neighborhoods"
        ordering = [
            "neighborhood_populated_place_id",
        ]

    def __str__(self):
        return "{}".format(
            self.neighborhood_name,
        )


#   ===================   #
#   Table name: Address   #
#   ===================   #
class Address(models.Model):
    address_id = models.AutoField(
        verbose_name="Address primary key (A.I)",
        primary_key=True,
    )

    address_name = models.CharField(
        verbose_name="Name of the address",
        max_length=50,
        blank=True,
        null=True,
    )

    address_acronym = models.CharField(
        verbose_name="Address acronym",
        max_length=5,
        blank=True,
        null=True,
    )

    address_status = models.BooleanField(
        verbose_name="Address status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = [
            "address_id",
        ]

    def __str__(self):
        return "{} | {}".format(
            self.address_acronym,
            self.address_name,
        )




#   =====================   #
#   Table name: BloodType   #
#   =====================   #
class BloodType(models.Model):
    blood_type_id = models.AutoField(
        verbose_name="Primary key of the Blood type (A.I)",
        primary_key=True,
    )

    blood_type_name = models.CharField(
        verbose_name="Blood type",
        max_length=5,
        blank=False,
        null=False,
    )

    blood_type_status = models.BooleanField(
        verbose_name="Status of the blood type for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Blood type"
        verbose_name_plural = "Blood types"
        ordering = [
            "blood_type_id",
        ]

    def __str__(self):
        return "{}".format(
            self.blood_type_name,
        )


#   ==================   #
#   Table name: Gender   #
#   ==================   #
class Gender(models.Model):
    gender_id = models.AutoField(
        verbose_name="Gender primary key (A.I)",
        primary_key=True,
    )

    gender_acronym = models.CharField(
        verbose_name="Gender acronym",
        max_length=3,
        blank=False,
        null=False,
    )

    gender_name = models.CharField(
        verbose_name="Name of the gender",
        max_length=50,
        blank=False,
        null=False,
    )

    gender_status = models.BooleanField(
        verbose_name="Gender status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"
        ordering = [
            "gender_id",
        ]

    def __str__(self):
        return "{}".format(
            self.gender_name,
        )


class Generation(models.Model):
    generation_id = models.AutoField(
        verbose_name="Generation primary key (A.I)",
        primary_key=True,
    )

    generation_name = models.CharField(
        verbose_name="Name of the generation",
        max_length=50,
        blank=False,
        null=False,
    )
    generation_start_year = models.PositiveSmallIntegerField(
        verbose_name="Start year of the generation",
        blank=True,
        null=True,
    )
    generation_end_year = models.PositiveSmallIntegerField(
        verbose_name="End year of the generation",
        blank=True,
        null=True,
    )

    generation_status = models.BooleanField(
        verbose_name="Generation status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Generation"
        verbose_name_plural = "Generations"
        ordering = [
            "generation_id",
        ]

    def __str__(self):
        return "{}".format(
            self.generation_name,
        )


#   ========================   #
#   Table name: DocumentType   #
#   ========================   #
class DocumentType(models.Model):
    document_type_id = models.AutoField(
        verbose_name="Primary key of the document type (A.I)",
        primary_key=True,
    )

    document_type_name = models.CharField(
        verbose_name="Name of the document type",
        max_length=31,
        blank=False,
        null=False,
    )

    document_type_acronym = models.CharField(
        verbose_name="Document type acronym",
        max_length=3,
        blank=False,
        null=False,
    )

    document_type_status = models.BooleanField(
        verbose_name="Document type status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Document type"
        verbose_name_plural = "Document types"
        ordering = [
            "document_type_id",
        ]

    def __str__(self):
        return "{}".format(
            self.document_type_name,
        )


#   ===========================   #
#   Table name: SignatureOption   #
#   ===========================   #
class SignatureOption(models.Model):
    sign_opt_id = models.AutoField(
        verbose_name="Primary key of the signature option (A.I)",
        primary_key=True,
    )

    sign_opt_name = models.CharField(
        verbose_name="Name of the signature option",
        max_length=31,
        blank=False,
        null=False,
    )

    sign_opt_status = models.BooleanField(
        verbose_name="Signature option status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Signature option"
        verbose_name_plural = "Signature options"
        ordering = [
            "sign_opt_id",
        ]

    def __str__(self):
        return "{}".format(
            self.sign_opt_name,
        )


#   =================   #
#   Table name: Group   #
#   =================   #
class Group(models.Model):
    group_id = models.AutoField(
        verbose_name="Group primary key (A.I)",
        primary_key=True,
    )

    group_registration_date = models.DateTimeField(
        verbose_name="Group registration date",
        auto_now=False,
        auto_now_add=True,
    )

    group_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    group_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    group_subscribers = models.PositiveIntegerField(
        verbose_name="Group subscribers",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    group_name = models.CharField(
        verbose_name="Name of the group",
        max_length=50,
        blank=False,
        null=False,
    )

    group_status = models.BooleanField(
        verbose_name="Group status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = [
            "group_id",
        ]

    def __str__(self):
        return "{}".format(
            self.group_name,
        )


#   ===================   #
#   Table name: Contact   #
#   ===================   #
class Contact(models.Model):
    contact_id = models.AutoField(
        verbose_name="Contact primary key (A.I)",
        primary_key=True,
    )

    contact_registration_date = models.DateTimeField(
        verbose_name="Contact registration date",
        auto_now=False,
        auto_now_add=True,
    )

    contact_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    contact_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    contact_names = models.CharField(
        verbose_name="Contact names",
        max_length=50,
        blank=False,
        null=False,
    )

    contact_surnames = models.CharField(
        verbose_name="Contact surnames",
        max_length=50,
        blank=False,
        null=False,
    )

    contact_cell_number = models.PositiveIntegerField(
        verbose_name="Contact cell phone number",
        blank=False,
        null=False,
        unique=True,
    )

    contact_email = models.EmailField(
        verbose_name="Contact e-mail address",
        blank=False,
        null=False,
        unique=True,
    )

    contact_status = models.BooleanField(
        verbose_name="Contact status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = [
            "-contact_date_update",
        ]

    def __str__(self):
        return "{} | {} {} | {} {} | {} | {}".format(
            self.contact_user,
            self.contact_names,
            self.contact_surnames,
            self.contact_cell_number,
            self.contact_email,
            self.contact_registration_date,
            self.contact_date_update,
        )


#   =====================   #
#   Table name: Directory   #
#   =====================   #
class Directory(models.Model):
    directory_id = models.AutoField(
        verbose_name="Directory primary key (A.I)",
        primary_key=True,
    )

    directory_registration_date = models.DateTimeField(
        verbose_name="Directory registration date",
        auto_now=False,
        auto_now_add=True,
    )

    directory_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    directory_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    directory_contact = models.ForeignKey(
        verbose_name="Directory contact",
        to=Contact,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    directory_group = models.ForeignKey(
        verbose_name="Directory group",
        to=Group,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    directory_status = models.BooleanField(
        verbose_name="Directory status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Directory"
        verbose_name_plural = "Directories"
        ordering = [
            "-directory_date_update",
        ]

    def __str__(self):
        return "{}".format(
            self.directory_contact,
        )


#   ==============================   #
#   Table name: CustomerDataUpdate   #
#   ==============================   #
class CustomerDataUpdate(models.Model):
    #   ===========   #
    #   System data   #
    #   ===========   #
    customer_data_update_id = models.AutoField(
        verbose_name="Customer primary key (A.I)",
        primary_key=True,
    )

    customer_data_update_registration_date = models.DateTimeField(
        verbose_name="Customer registration date",
        auto_now=False,
        auto_now_add=True,
    )

    customer_data_update_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    #   ===================   #
    #   Basic customer data   #
    #   ===================   #

    customer_data_update_document_number = models.PositiveIntegerField(
        verbose_name="Customer document number",
        blank=False,
        null=False,
        unique=True,
    )

    customer_data_update_first_name = models.CharField(
        verbose_name="Customer first name",
        max_length=50,
        blank=False,
        null=False,
    )

    customer_data_update_middle_name = models.CharField(
        verbose_name="Customer middle name",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_data_update_first_surname = models.CharField(
        verbose_name="Customer first surname",
        max_length=50,
        blank=False,
        null=False,
    )

    customer_data_update_second_surname = models.CharField(
        verbose_name="Customer second surname",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_data_update_gender = models.ForeignKey(
        verbose_name="Customer gender",
        to=Gender,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=3,
    )

    customer_data_means_of_transport = models.ForeignKey(
        verbose_name="Mean of transport",
        to=MeansOfTransport,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_data_update_date_birth = models.DateField(
        verbose_name="Customer date of birth",
        blank=False,
        null=False,
    )
    #   ============================   #
    #   Customer contact information   #
    #   ============================   #
    customer_data_update_cell_number = models.PositiveIntegerField(
        verbose_name="Customer cell phone number", blank=False, null=False, default=0
    )

    customer_data_update_email = models.EmailField(
        verbose_name="Customer e-mail address",
        blank=True,
        null=True,
        unique=True,
    )
    #   ===========   #
    #   Habeas data   #
    #   ===========   #
    customer_data_update_agree_to_the_terms = models.BooleanField(
        verbose_name="Agree to the terms",
        blank=False,
        null=False,
        default=False,
    )

    #   =============================   #
    #   Customer location information   #
    #   =============================   #
    customer_data_update_neighborhood = models.ForeignKey(
        verbose_name="Customer neighborhood",
        to=Neighborhood,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_data_update_residence_address_select = models.ForeignKey(
        verbose_name="Customer residence address select",
        to=Address,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_data_update_residence_address_part_one = models.CharField(
        verbose_name="Customer residence address part one",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_data_update_residence_address_part_two = models.CharField(
        verbose_name="Customer residence address part two",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_data_update_residence_address_part_three = models.CharField(
        verbose_name="Customer residence address part three",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_data_update_residence_address_supplementary_part = models.CharField(
        verbose_name="Customer residence address supplementary part",
        max_length=50,
        blank=True,
        null=True,
    )

    #   ==================   #
    #   Supplementary Data   #
    #   ==================   #
    customer_data_update_children_sw = models.BooleanField(
        verbose_name="Does the customer have children",
        blank=False,
        null=False,
        default=False,
    )

    customer_data_update_pets_sw = models.BooleanField(
        verbose_name="Does the customer have pets",
        blank=False,
        null=False,
        default=False,
    )

    customer_data_update_marital_status = models.ForeignKey(
        verbose_name="Customer marital status",
        to=MaritalStatus,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_data_update_status = models.BooleanField(
        verbose_name="Customer status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Customer data update"
        verbose_name_plural = "Customers data update"
        ordering = [
            "-customer_data_update_id",
        ]

    def __str__(self):
        return "{} | {} {} | {}".format(
            self.customer_data_update_document_number,
            self.customer_data_update_first_name,
            self.customer_data_update_first_surname,
            self.customer_data_update_registration_date,
        )


#   ====================   #
#   Table name: Customer   #
#   ====================   #
class Customer(models.Model):
    #   ===========   #
    #   System data   #
    #   ===========   #
    customer_id = models.AutoField(
        verbose_name="Customer primary key (A.I)",
        primary_key=True,
    )

    customer_registration_date = models.DateTimeField(
        verbose_name="Customer registration date",
        auto_now=False,
        auto_now_add=True,
    )

    customer_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    customer_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    customer_points = models.PositiveIntegerField(
        verbose_name="Customer points",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    customer_invoices = models.PositiveIntegerField(
        verbose_name="Customer invoices",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    customer_purchases = models.BigIntegerField(
        verbose_name="Customer purchases",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    customer_signature_option = models.ForeignKey(
        verbose_name="Signature option",
        to=SignatureOption,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_signature_desc = models.CharField(
        verbose_name="Signature description",
        max_length=255,
        blank=True,
        null=True,
    )
    #   ===================   #
    #   Basic customer data   #
    #   ===================   #
    customer_document_type = models.ForeignKey(
        verbose_name="Type of customer document",
        to=DocumentType,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        default=1,
    )

    customer_document_number = models.PositiveIntegerField(
        verbose_name="Customer document number",
        blank=False,
        null=False,
        unique=True,
    )

    customer_first_name = models.CharField(
        verbose_name="Customer first name",
        max_length=50,
        blank=False,
        null=False,
    )

    customer_middle_name = models.CharField(
        verbose_name="Customer middle name",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_first_surname = models.CharField(
        verbose_name="Customer first surname",
        max_length=50,
        blank=False,
        null=False,
    )

    customer_second_surname = models.CharField(
        verbose_name="Customer second surname",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_gender = models.ForeignKey(
        verbose_name="Customer gender",
        to=Gender,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=3,
    )

    customer_date_birth = models.DateField(
        verbose_name="Customer date of birth",
        blank=False,
        null=False,
    )

    customer_blood_type = models.ForeignKey(
        verbose_name="Customer blood type",
        to=BloodType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    #   ============================   #
    #   Customer contact information   #
    #   ============================   #
    customer_cell_number = models.PositiveIntegerField(
        verbose_name="Customer cell phone number", blank=False, null=False, default=0
    )

    customer_landline_number = models.PositiveIntegerField(
        verbose_name="Customer Landline phone number",
        blank=True,
        null=True,
    )

    customer_email = models.EmailField(
        verbose_name="Customer e-mail address",
        blank=True,
        null=True,
        unique=True,
    )
    #   =============================   #
    #   Customer location information   #
    #   =============================   #
    customer_neighborhood = models.ForeignKey(
        verbose_name="Customer neighborhood",
        to=Neighborhood,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_residence_address_select = models.ForeignKey(
        verbose_name="Customer residence address select",
        to=Address,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_residence_address_part_one = models.CharField(
        verbose_name="Customer residence address part one",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_residence_address_part_two = models.CharField(
        verbose_name="Customer residence address part two",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_residence_address_part_three = models.CharField(
        verbose_name="Customer residence address part three",
        max_length=10,
        blank=True,
        null=True,
    )

    customer_residence_address_supplementary_part = models.CharField(
        verbose_name="Customer residence address supplementary part",
        max_length=50,
        blank=True,
        null=True,
    )
    #   ==============================   #
    #   Aditional customer information   #
    #   ==============================   #
    customer_social_class = models.PositiveSmallIntegerField(
        verbose_name="Customer social class",
        blank=True,
        null=True,
    )

    customer_marital_status = models.ForeignKey(
        verbose_name="Customer marital status",
        to=MaritalStatus,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    customer_occupation = models.CharField(
        verbose_name="Customer occupation",
        max_length=50,
        blank=True,
        null=True,
    )

    #   ========================   #
    #   Customer social networks   #
    #   ========================   #
    customer_facebook = models.BooleanField(
        verbose_name="Facebook",
        blank=False,
        null=False,
        default=False,
    )

    customer_instagram = models.BooleanField(
        verbose_name="Instagram",
        blank=False,
        null=False,
        default=False,
    )

    customer_twitter = models.BooleanField(
        verbose_name="Twitter",
        blank=False,
        null=False,
        default=False,
    )

    customer_whatsapp = models.BooleanField(
        verbose_name="WhatsApp",
        blank=False,
        null=False,
        default=False,
    )
    #   ===========   #
    #   Habeas data   #
    #   ===========   #
    customer_notifications_email = models.BooleanField(
        verbose_name="Notifications to the customer e-mail address",
        blank=False,
        null=False,
        default=False,
    )

    customer_notifications_cell = models.BooleanField(
        verbose_name="Notifications to the customer cell phone number",
        blank=False,
        null=False,
        default=False,
    )

    customer_notifications_residence_address = models.BooleanField(
        verbose_name="Notifications to the customer residence address",
        blank=False,
        null=False,
        default=False,
    )
    #   ==================   #
    #   Supplementary Data   #
    #   ==================   #
    customer_children_sw = models.BooleanField(
        verbose_name="Does the customer have children",
        blank=False,
        null=False,
        default=False,
    )

    customer_vehicles_sw = models.BooleanField(
        verbose_name="Does the customer have vehicles",
        blank=False,
        null=False,
        default=False,
    )

    customer_pets_sw = models.BooleanField(
        verbose_name="Does the customer have pets",
        blank=False,
        null=False,
        default=False,
    )
    #   ======================================   #
    #   Customer emergency contact information   #
    #   ======================================   #
    customer_health_plan = models.ForeignKey(
        verbose_name="Customer health plan",
        to=HealthPlan,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=1,
    )

    customer_children_number = models.PositiveIntegerField(
        verbose_name="Number of children",
        blank=True,
        null=True,
    )

    customer_emergency_contact_names = models.CharField(
        verbose_name="Customer emergency contact names",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_emergency_contact_surnames = models.CharField(
        verbose_name="Customer emergency contact surnames",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_emergency_contact_number = models.PositiveIntegerField(
        verbose_name="Customer emergency contact number",
        blank=True,
        null=True,
    )

    customer_covenant = models.CharField(
        verbose_name="Customer sport covenant",
        max_length=50,
        blank=True,
        null=True,
    )

    customer_internal = models.BooleanField(
        verbose_name="Internal customer",
        blank=False,
        null=False,
        default=False,
    )

    customer_status = models.BooleanField(
        verbose_name="Customer status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = [
            "-customer_purchases",
        ]

    def __str__(self):
        return "{} | {} {} | {}".format(
            self.customer_document_number,
            self.customer_first_surname,
            self.customer_first_name,
            self.customer_registration_date,
        )


#   =====================================   #
#   Table name: CustomerFamilyInformation   #
#   =====================================   #
class CustomerFamilyInformation(models.Model):
    family_id = models.AutoField(
        verbose_name="Primary key of the customer family member (A.I)",
        primary_key=True,
    )

    family_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    family_names = models.CharField(
        verbose_name="Names of the customer family member",
        max_length=50,
        blank=False,
        null=False,
    )

    family_surnames = models.CharField(
        verbose_name="Surnames of the customer family member",
        max_length=50,
        blank=False,
        null=False,
    )

    family_date_birth = models.DateField(
        verbose_name="Date of birth of the customer family member",
        blank=False,
        null=False,
    )

    family_kinship = models.ForeignKey(
        verbose_name="Customer kinship",
        to=Kinship,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    family_customer = models.ForeignKey(
        verbose_name="Customer associated with a family member",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    family_status = models.BooleanField(
        verbose_name="Status of the customer family member for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Customer family information"
        verbose_name_plural = "Customer family information"
        ordering = [
            "family_customer_id",
        ]

    def __str__(self):
        return "{} {} | {} => {}".format(
            self.family_surnames,
            self.family_names,
            self.family_kinship,
            self.family_customer,
        )


#   =======================   #
#   Table name: CustomerPet   #
#   =======================   #
class CustomerPet(models.Model):
    pet_id = models.AutoField(
        verbose_name="Pet primary key (A.I)",
        primary_key=True,
    )

    pet_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    pet_type = models.ForeignKey(
        verbose_name="Pet type",
        to=TypeOfPets,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    pet_customer = models.ForeignKey(
        verbose_name="Customer associated with a pet",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    pet_status = models.BooleanField(
        verbose_name="Pet status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Customer pet"
        verbose_name_plural = "Customer pets"
        ordering = [
            "pet_customer_id",
        ]

    def __str__(self):
        return "{} => {}".format(
            self.pet_type,
            self.pet_customer,
        )


#   ===========================   #
#   Table name: CustomerVehicle   #
#   ===========================   #
class CustomerVehicle(models.Model):
    vehicle_id = models.AutoField(
        verbose_name="Primary key of the customer vehicle (A.I)",
        primary_key=True,
    )

    vehicle_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    vehicle_type = models.ForeignKey(
        verbose_name="Type of vehicle",
        to=TypeOfVehicle,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    vehicle_customer = models.ForeignKey(
        verbose_name="Customer associated with a vehicle",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    vehicle_registration_plate = models.CharField(
        verbose_name="Customer vehicle registration number",
        max_length=6,
        blank=True,
        null=True,
    )

    vehicle_status = models.BooleanField(
        verbose_name="Vehicle status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Customer vehicle"
        verbose_name_plural = "Customer vehicles"
        ordering = [
            "vehicle_customer_id",
        ]

    def __str__(self):
        return "{} | {} => {}".format(
            self.vehicle_type,
            self.vehicle_registration_plate,
            self.vehicle_customer,
        )


##############################
## Commercial premises data ##
##############################


#   =================   #
#   Table name: Owner   #
#   =================   #
class Owner(models.Model):
    owner_id = models.AutoField(
        verbose_name="Owner primary key (A.I)",
        primary_key=True,
    )

    owner_document_type = models.ForeignKey(
        verbose_name="Type of owner document",
        to=DocumentType,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        default=1,
    )

    owner_document_number = models.PositiveIntegerField(
        verbose_name="Owner document number",
        blank=False,
        null=False,
        unique=True,
    )

    owner_names = models.CharField(
        verbose_name="Owner names",
        max_length=50,
        blank=False,
        null=False,
    )

    owner_surnames = models.CharField(
        verbose_name="Owner surnames",
        max_length=50,
        blank=False,
        null=False,
    )

    owner_cell_number = models.PositiveIntegerField(
        verbose_name="Owner cell phone number",
        blank=False,
        null=False,
    )

    owner_status = models.BooleanField(
        verbose_name="Owner status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"
        ordering = [
            "owner_id",
        ]

    def __str__(self):
        return "{} | {} {} | {}".format(
            self.owner_document_number,
            self.owner_surnames,
            self.owner_names,
            self.owner_cell_number,
        )


#   =====================================   #
#   Table name: CommercialPremiseCategory   #
#   =====================================   #
class CommercialPremiseCategory(models.Model):
    commercial_category_id = models.AutoField(
        verbose_name="Primary key of the commercial premise category (A.I)",
        primary_key=True,
    )

    commercial_category_name = models.CharField(
        verbose_name="Name of the commercial premise category",
        max_length=100,
        blank=False,
        null=False,
    )

    commercial_category_status = models.BooleanField(
        verbose_name="Status of the commercial premise category for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Commercial premise category"
        verbose_name_plural = "Commercial premise categories"
        ordering = [
            "commercial_category_id",
        ]

    def __str__(self):
        return "{}".format(
            self.commercial_category_name,
        )


#   =============================   #
#   Table name: CommercialPremise   #
#   =============================   #
class CommercialPremise(models.Model):
    commercial_premise_id = models.AutoField(
        verbose_name="Primary key of the commercial premise (A.I)",
        primary_key=True,
    )

    commercial_premise_invoices = models.PositiveIntegerField(
        verbose_name="Commercial premise invoices",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    commercial_premise_name = models.CharField(
        verbose_name="Name of the commercial premise",
        max_length=100,
        blank=False,
        null=False,
    )

    commercial_premise_nomenclature = models.CharField(
        verbose_name="Nomenclature of the commercial premise",
        max_length=25,
        blank=False,
        null=False,
    )

    commercial_premise_category = models.ForeignKey(
        verbose_name="Category of the commercial premise",
        to=CommercialPremiseCategory,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    commercial_premise_anchor = models.BooleanField(
        verbose_name="Is the commercial premises an anchor",
        blank=False,
        null=False,
        default=False,
    )

    commercial_premise_purchase = models.BigIntegerField(
        verbose_name="Accumulated purchase",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    commercial_premise_owner = models.ForeignKey(
        verbose_name="Owner associated with the commercial premise",
        to=Owner,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    commercial_premise_status = models.BooleanField(
        verbose_name="Status of the commercial premise for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Commercial premise"
        verbose_name_plural = "Commercial premises"
        ordering = [
            "-commercial_premise_purchase",
        ]

    def __str__(self):
        return "{} | {} | {}".format(
            self.commercial_premise_name,
            self.commercial_premise_nomenclature,
            self.commercial_premise_category,
        )

###################
## Invoices data ##
###################


#   =========================   #
#   Table name: PaymentMethod   #
#   =========================   #
class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(
        verbose_name="Primary key of the payment method (A.I)",
        primary_key=True,
    )

    payment_method_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    payment_method_registration_date = models.DateTimeField(
        verbose_name="Payment method registration date",
        auto_now=False,
        auto_now_add=True,
    )

    payment_method_update_date = models.DateTimeField(
        verbose_name="Payment method update date",
        auto_now=True,
    )

    payment_method_code = models.PositiveIntegerField(
        verbose_name="Payment method type code",
        blank=False,
        null=False,
        unique=True,
        editable=True,
        
    )

    payment_method_name = models.CharField(
        verbose_name="Name of the payment method",
        max_length=50,
        blank=False,
        null=False,
    )

    payment_method_status = models.BooleanField(
        verbose_name="Status of the payment method for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Payment method"
        verbose_name_plural = "Payment methods"
        ordering = [
            "payment_method_name",
        ]

    def __str__(self):
        return "{}".format(
            self.payment_method_name,
        )


#   ============================   #
#   Table name: RegulatoryAgency   #
#   ============================   #
class RegulatoryAgency(models.Model):
    regulatory_agency_id = models.AutoField(
        verbose_name="Primary key of the regulatory agency (A.I)",
        primary_key=True,
    )

    regulatory_agency_name = models.CharField(
        verbose_name="Name of the regulatory agency",
        max_length=50,
        blank=False,
        null=False,
    )

    regulatory_agency_image = models.ImageField(
        verbose_name="Regulatory agency image",
        upload_to="regulatory_agency/",
        blank=False,
        null=False,
    )

    regulatory_agency_status = models.BooleanField(
        verbose_name="Status of the regulatory agency for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Regulatory agency"
        verbose_name_plural = "Regulatory agencies"
        ordering = [
            "regulatory_agency_id",
        ]

    def __str__(self):
        return "{}".format(
            self.regulatory_agency_name,
        )


#   ========================   #
#   Table name: CampaignType   #
#   ========================   #
class CampaignType(models.Model):
    campaign_type_id = models.AutoField(
        verbose_name="Primary key of the campaign type (A.I)",
        primary_key=True,
    )

    campaign_type_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    campaign_type_registration_date = models.DateTimeField(
        verbose_name="Campaign type registration date",
        auto_now=False,
        auto_now_add=True,
    )

    campaign_type_update_date = models.DateTimeField(
        verbose_name="Campaign type update date",
        auto_now=True,
    )

    campaign_type_code = models.PositiveIntegerField(
        verbose_name="Campaign type code",
        blank=False,
        null=False,
        unique=True,
        editable=False,
        default=10,
    )

    campaign_type_name = models.CharField(
        verbose_name="Name of the campaign type",
        max_length=100,
        blank=False,
        null=False,
    )

    campaign_type_spanish_name = models.CharField(
        verbose_name="Name of the campaign type (Spanish)",
        max_length=100,
        blank=False,
        null=False,
    )

    campaign_type_status = models.BooleanField(
        verbose_name="Status of the campaign type for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Campaign Type"
        verbose_name_plural = "Campaign Types"
        ordering = [
            "campaign_type_name",
        ]

    def __str__(self):
        return "{}".format(
            self.campaign_type_spanish_name,
        )


#   ====================   #
#   Table name: Campaign   #
#   ====================   #
class Campaign(models.Model):
    campaign_id = models.AutoField(
        verbose_name="Campaign primary key (A.I)",
        primary_key=True,
    )

    campaign_invoices_number = models.PositiveIntegerField(
        verbose_name="Number of accumulated invoices",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    campaign_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    campaign_registration_date = models.DateTimeField(
        verbose_name="Campaign registration date",
        auto_now=False,
        auto_now_add=True,
    )

    campaign_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    campaign_name = models.CharField(
        verbose_name="Campaign name",
        max_length=50,
        blank=False,
        null=False,
    )

    campaign_type = models.ForeignKey(
        verbose_name="Campaign type",
        to=CampaignType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    campaign_award_title = models.CharField(
        verbose_name="Campaign award title",
        max_length=50,
        blank=True,
        null=True,
    )

    campaign_award_description = models.CharField(
        verbose_name="Campaign award description",
        max_length=250,
        blank=True,
        null=True,
    )

    campaign_start_date = models.DateField(
        verbose_name="Campaign start date",
        blank=False,
        null=False,
        default=date_today(),
    )

    campaign_end_date = models.DateField(
        verbose_name="Campaign end date",
        blank=False,
        null=False,
        default=date_today(),
    )

    campaign_start_time_window = models.TimeField(
        verbose_name="Campaign start time window",
        blank=False,
        null=False,
        default="00:00",
    )

    campaign_end_time_window = models.TimeField(
        verbose_name="Campaign end time window",
        blank=False,
        null=False,
        default="23:59",
    )

    campaign_monday = models.BooleanField(
        verbose_name="Monday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_tuesday = models.BooleanField(
        verbose_name="Tuesday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_wednesday = models.BooleanField(
        verbose_name="Wednesday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_thursday = models.BooleanField(
        verbose_name="Thursday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_friday = models.BooleanField(
        verbose_name="Friday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_saturday = models.BooleanField(
        verbose_name="Saturday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_sunday = models.BooleanField(
        verbose_name="Sunday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus = models.BooleanField(
        verbose_name="The campaign allows the bonus",
        blank=False,
        null=False,
        default=False,
    )

    campaign_bonus_start_date = models.DateField(
        verbose_name="Bonus Campaign start date",
        blank=False,
        null=False,
        default=date_today(),
    )

    campaign_bonus_end_date = models.DateField(
        verbose_name="Bonus Campaign end date",
        blank=False,
        null=False,
        default=date_today(),
    )

    campaign_bonus_start_time_window = models.TimeField(
        verbose_name="Bonus Campaign start time window",
        blank=False,
        null=False,
        default="00:00",
    )

    campaign_bonus_end_time_window = models.TimeField(
        verbose_name="Bonus Campaign end time window",
        blank=False,
        null=False,
        default="23:59",
    )

    campaign_bonus_monday = models.BooleanField(
        verbose_name="Bonus Monday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_tuesday = models.BooleanField(
        verbose_name="Bonus Tuesday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_wednesday = models.BooleanField(
        verbose_name="Bonus Wednesday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_thursday = models.BooleanField(
        verbose_name="Bonus Thursday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_friday = models.BooleanField(
        verbose_name="Bonus Friday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_saturday = models.BooleanField(
        verbose_name="Bonus Saturday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_sunday = models.BooleanField(
        verbose_name="Bonus Sunday enabled",
        blank=False,
        null=False,
        default=True,
    )

    campaign_bonus_ticket_multiplier = models.PositiveIntegerField(
        verbose_name="Bonus Ticket multiplier",
        blank=False,
        null=False,
        default=1,
    )

    campaign_minimum_purchase_value = models.PositiveIntegerField(
        verbose_name="Minimum purchase value",
        blank=False,
        null=False,
        default=50,
    )

    campaign_minimum_purchase_value_anchor = models.PositiveIntegerField(
        verbose_name="Minimum purchase value anchor",
        blank=False,
        null=False,
        default=50,
    )

    campaign_ticket_multiplier = models.PositiveIntegerField(
        verbose_name="Ticket multiplier",
        blank=False,
        null=False,
        default=1,
    )

    campaign_maximum_tickets_bingo_cards_campaign = models.PositiveIntegerField(
        verbose_name="Maximum number of tickets or bingo cards per campaign",
        blank=True,
        null=True,
    )

    campaign_maximum_tickets_bingo_cards_customer = models.PositiveIntegerField(
        verbose_name="Maximum number of tickets or bingo cards per customer",
        blank=True,
        null=True,
    )

    campaign_maximum_tickets_bingo_cards_invoice = models.PositiveIntegerField(
        verbose_name="Maximum number of tickets or bingo cards per invoice",
        blank=True,
        null=True,
    )

    campaign_minimum_accumulated_value_per_invoice = models.PositiveIntegerField(
        verbose_name="Minimum number of accumulated value per invoice",
        blank=False,
        null=False,
        default=0,
    )

    campaign_maximum_tickets_bingo_cards_campaign_sw = models.BooleanField(
        verbose_name="The campaign allows limiting the number of tickets or bingo cards per campaign",
        blank=False,
        null=False,
        default=True,
    )

    campaign_maximum_tickets_bingo_cards_customer_sw = models.BooleanField(
        verbose_name="The campaign allows limiting the number of tickets or bingo cards per customer",
        blank=False,
        null=False,
        default=True,
    )

    campaign_maximum_tickets_bingo_cards_invoice_sw = models.BooleanField(
        verbose_name="The campaign allows limiting the number of tickets or bingo cards per invoice",
        blank=False,
        null=False,
        default=True,
    )

    campaign_record_after_maximum_tickets_bingo_cards = models.BooleanField(
        verbose_name="The campaign allows record invoices after the maximum number of tickets or bingo cards have been issued.",
        blank=False,
        null=False,
        default=False,
    )

    campaign_record_api = models.BooleanField(
        verbose_name="The campaign allows record invoices online.",
        blank=False,
        null=False,
        default=False,
    )

    campaign_multiplier_local = models.BooleanField(
        verbose_name="The campaign allows record individual multiplier.",
        blank=False,
        null=False,
        default=False,
    )

    campaign_image = models.ImageField(
        verbose_name="Campaign image",
        upload_to="campaign/",
        blank=False,
        null=False,
    )

    campaign_regulatory_agency = models.ForeignKey(
        verbose_name="Campaign regulatory agency",
        to=RegulatoryAgency,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    campaign_counter = models.PositiveIntegerField(
        verbose_name="Campaign counter",
        blank=False,
        null=False,
        default=0,
    )

    campaign_internal = models.BooleanField(
        verbose_name="Internal campaign",
        blank=False,
        null=False,
        default=False,
    )

    campaign_male = models.BooleanField(
        verbose_name="The campaign allows male participants",
        blank=False,
        null=False,
        default=True,
    )

    campaign_female = models.BooleanField(
        verbose_name="The campaign allows female participants",
        blank=False,
        null=False,
        default=True,
    )

    campaign_accumulation = models.BooleanField(
        verbose_name="The campaign allows the accumulation of surplus values from invoices",
        blank=False,
        null=False,
        default=True,
    )

    campaign_delete_accumulation = models.BooleanField(
        verbose_name="The campaign allows the elimination of surplus values from previous days invoices",
        blank=False,
        null=False,
        default=False,
    )

    campaign_print_ticket = models.BooleanField(
        verbose_name="The campaign allows the printing of tickets",
        blank=False,
        null=False,
    )

    campaign_award = models.BooleanField(
        verbose_name="The campaign allows the award",
        blank=False,
        null=False,
        default=True,
    )

    campaign_minimum_age = models.PositiveIntegerField(
        verbose_name="Minimum age of customer",
        blank=False,
        null=False,
        default=0,
    )

    campaign_maximum_age = models.PositiveIntegerField(
        verbose_name="Maximum age of customer",
        blank=False,
        null=False,
        default=150,
    )

    campaign_excludes = models.TextField(
        verbose_name="Campaign excludes",
        blank=True,
        null=True,
    )

    campaign_multiplier_local_x2 = models.TextField(
        verbose_name="Multiplier local x2",
        blank=True,
        null=True,
    )

    campaign_multiplier_local_x3 = models.TextField(
        verbose_name="Multiplier local x3",
        blank=True,
        null=True,
    )

    campaign_multiplier_local_x4 = models.TextField(
        verbose_name="Multiplier local x4",
        blank=True,
        null=True,
    )

    campaign_multiplier_local_x5 = models.TextField(
        verbose_name="Multiplier local x5",
        blank=True,
        null=True,
    )

    campaign_ticket_title = models.BooleanField(
        verbose_name="The campaign ticket allows title",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_award = models.BooleanField(
        verbose_name="The campaign ticket allows award",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_award_description = models.BooleanField(
        verbose_name="The campaign ticket allows award description",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_validity_date = models.BooleanField(
        verbose_name="The campaign ticket allows validity date",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_document_number = models.BooleanField(
        verbose_name="The campaign ticket allows document number",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_names = models.BooleanField(
        verbose_name="The campaign ticket allows names",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_birth_day = models.BooleanField(
        verbose_name="The campaign ticket allows birth day",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_cell_number = models.BooleanField(
        verbose_name="The campaign ticket allows cell number",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_email = models.BooleanField(
        verbose_name="The campaign ticket allows email",
        blank=False,
        null=False,
        default=False,
    )

    campaign_ticket_regulatory_agency = models.BooleanField(
        verbose_name="The campaign ticket allows regulatory agency",
        blank=False,
        null=False,
        default=False,
    )

    campaign_status = models.BooleanField(
        verbose_name="Campaign status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
        ordering = [
            "campaign_id",
        ]

    def __str__(self):
        return "{} | {} | {}".format(
            self.campaign_name,
            self.campaign_start_date,
            self.campaign_end_date,
        )

    @property
    def is_active(self):
        """Check if the campaign is active based on current date, time, and day"""
        from django.utils import timezone
        now = timezone.now()
        today = now.date()
        current_time = now.time()
        current_weekday = now.weekday()  # 0=Monday, 6=Sunday
        
        # Check date range
        if not (self.campaign_start_date <= today <= self.campaign_end_date):
            return False
        
        # Check time window
        if not (self.campaign_start_time_window <= current_time <= self.campaign_end_time_window):
            return False
        
        # Check day of week
        day_enabled = [
            self.campaign_monday,    # 0
            self.campaign_tuesday,   # 1
            self.campaign_wednesday, # 2
            self.campaign_thursday,  # 3
            self.campaign_friday,    # 4
            self.campaign_saturday,  # 5
            self.campaign_sunday,    # 6
        ][current_weekday]
        
        return day_enabled

    @property
    def days_remaining(self):
        """Calculate days remaining until campaign ends"""
        from django.utils import timezone
        today = timezone.now().date()
        if today > self.campaign_end_date:
            return 0
        return (self.campaign_end_date - today).days


#   ===================   #
#   Table name: Invoice   #
#   ===================   #
class Invoice(models.Model):
    invoice_id = models.AutoField(
        verbose_name="Invoice primary key (A.I)",
        primary_key=True,
    )

    invoice_user = models.CharField(
        verbose_name="User who created or modified the record",
        max_length=50,
        blank=False,
        null=False,
        default="-",
        editable=False,
    )

    invoice_registration_date = models.DateTimeField(
        verbose_name="Invoice registration date",
        auto_now=False,
        auto_now_add=True,
    )

    invoice_purchase_date = models.DateField(
        verbose_name="Date of invoice purchase",
        blank=False,
        null=False,
    )

    invoice_customer = models.ForeignKey(
        verbose_name="Customer associated to the invoice",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    invoice_number = models.CharField(
        verbose_name="Invoice number",
        max_length=50,
        blank=True,
        null=True,
    )

    invoice_time_of_stay = models.PositiveIntegerField(
        verbose_name="Time of stay",
        blank=False,
        null=False,
        default=0,
    )

    invoice_purchase_value = models.PositiveIntegerField(
        verbose_name="Purchase value",
        blank=False,
        null=False,
    )

    invoice_commercial_premise = models.ForeignKey(
        verbose_name="Commercial premise to which the invoice belongs",
        to=CommercialPremise,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    invoice_payment_method = models.ForeignKey(
        verbose_name="Method of invoice payment",
        to=PaymentMethod,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    invoice_parking = models.BooleanField(
        verbose_name="Invoice redeemed by the customer to cover parking costs",
        blank=False,
        null=False,
        default=False,
    )

    invoice_status = models.BooleanField(
        verbose_name="Invoice status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        ordering = [
            "-invoice_purchase_value",
        ]

    def __str__(self):
        return "{} | {} | {}".format(
            self.invoice_commercial_premise,
            self.invoice_purchase_date,
            self.invoice_purchase_value,
        )


#   ==================================   #
#   Table name: InvoiceForEachCampaign   #
#   ==================================   #
class InvoiceForEachCampaign(models.Model):
    invoice_for_each_campaign_id = models.AutoField(
        verbose_name="Invoice for each campaign primary key (A.I)",
        primary_key=True,
    )

    invoice_for_each_campaign_invoice = models.ForeignKey(
        verbose_name="Invoice associated to the campaign",
        to=Invoice,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    invoice_for_each_campaign_campaign = models.ForeignKey(
        verbose_name="Campaign associated to the invoice",
        to=Campaign,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    invoice_status = models.BooleanField(
        verbose_name="Invoice for each campaign status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Invoice for each campaign"
        verbose_name_plural = "Invoices for each campaign"
        ordering = [
            "invoice_for_each_campaign_id",
        ]

    def __str__(self):
        return "{} | {}".format(
            self.invoice_for_each_campaign_invoice,
            self.invoice_for_each_campaign_campaign,
        )


#   ========================   #
#   Table name: Accumulation   #
#   ========================   #
class Accumulation(models.Model):
    accumulation_id = models.AutoField(
        verbose_name="Accumulation primary key (A.I)",
        primary_key=True,
    )

    accumulation_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    accumulation_purchase = models.BigIntegerField(
        verbose_name="Accumulated purchase",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    accumulation_ticket = models.PositiveIntegerField(
        verbose_name="Accumulated ticket number",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    accumulation_value = models.PositiveIntegerField(
        verbose_name="Accumulated value",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    accumulation_customer = models.ForeignKey(
        verbose_name="Customer associated with the accumulation value",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    accumulation_campaign = models.ForeignKey(
        verbose_name="Customer associated to the accumulated value",
        to=Campaign,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    accumulation_status = models.BooleanField(
        verbose_name="Accumulation status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Accumulated value"
        verbose_name_plural = "Accumulated values"
        ordering = [
            "-accumulation_date_update",
        ]

    def __str__(self):
        return "{} | {} | {} => {}".format(
            self.accumulation_date_update,
            self.accumulation_campaign,
            self.accumulation_value,
            self.accumulation_customer,
        )


#   ==============================   #
#   Table name: AnchorAccumulation   #
#   ==============================   #
class AnchorAccumulation(models.Model):
    anchor_accumulation_id = models.AutoField(
        verbose_name="Accumulation primary key (A.I)",
        primary_key=True,
    )

    anchor_accumulation_date_update = models.DateTimeField(
        verbose_name="Date of update",
        auto_now=True,
    )

    anchor_accumulation_value = models.PositiveIntegerField(
        verbose_name="Accumulated value",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    anchor_accumulation_customer = models.ForeignKey(
        verbose_name="Customer associated with the accumulation value",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    anchor_accumulation_campaign = models.ForeignKey(
        verbose_name="Customer associated to the accumulated value",
        to=Campaign,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    anchor_accumulation_status = models.BooleanField(
        verbose_name="Accumulation status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Anchor accumulated value"
        verbose_name_plural = "Anchor accumulated values"
        ordering = [
            "-anchor_accumulation_date_update",
        ]

    def __str__(self):
        return "{} | {} | {} => {}".format(
            self.anchor_accumulation_date_update,
            self.anchor_accumulation_campaign,
            self.anchor_accumulation_value,
            self.anchor_accumulation_customer,
        )

#   ==================   #
#   Table name: Ticket   #
#   ==================   #
class Ticket(models.Model):
    ticket_id = models.AutoField(
        verbose_name="Tickets primary key (A.I)",
        primary_key=True,
    )

    ticket_registration_date = models.DateTimeField(
        verbose_name="Ticket registration date",
        auto_now=False,
        auto_now_add=True,
    )

    ticket_value = models.PositiveIntegerField(
        verbose_name="Accumulated value",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_anchor_value = models.PositiveIntegerField(
        verbose_name="Accumulated anchor value",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_campaign_value = models.PositiveIntegerField(
        verbose_name="Accumulated campaign value",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_customer = models.ForeignKey(
        verbose_name="Customer associated with the tickets",
        to=Customer,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    ticket_campaign = models.ForeignKey(
        verbose_name="Campaign associated with the tickets",
        to=Campaign,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    ticket_total = models.PositiveIntegerField(
        verbose_name="Total tickets",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_opening = models.PositiveIntegerField(
        verbose_name="Opening ticket",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_closing = models.PositiveIntegerField(
        verbose_name="Closing ticket",
        blank=False,
        null=False,
        default=0,
        editable=False,
    )

    ticket_status = models.BooleanField(
        verbose_name="Tickets status for logical elimination",
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = "Ticket value"
        verbose_name_plural = "Ticket values"
        ordering = [
            "-ticket_registration_date",
        ]

    def __str__(self):
        return "{} | {} | {} | {} => {}".format(
            self.ticket_campaign,
            self.ticket_value,
            self.ticket_anchor_value,
            self.ticket_campaign_value,
            self.ticket_customer,
        )

