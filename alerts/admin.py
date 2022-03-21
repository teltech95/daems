# from django.contrib import admin
# from django.contrib.auth.models import Group
# from .models import DisasterAlerts
# # Register your models here.
# import csv
# from django.http import HttpResponse


# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):

#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
#             meta)
#         writer = csv.writer(response)

#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field)
#                                   for field in field_names])

#         return response

#     export_as_csv.short_description = "Export Selected"


# class detailsAdmin(admin.ModelAdmin, ExportCsvMixin):
#     list_display = ("event_title", "event_type",
#                     "location", "createAt", "expected_date")
#     list_filter = ('event_type', 'location',  'createAt')
#     search_fields = ('event_title',)
#     actions = ["export_as_csv"]


# admin.site.register(DisasterAlerts, detailsAdmin)
# admin.site.unregister(Group)
