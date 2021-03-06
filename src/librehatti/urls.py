from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from reports.register_generator import GenerateRegister
from reports.search import SearchResult
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'librehatti.catalog.views.index'),
    url(r'^catalog/', include('librehatti.catalog.urls')),
    url(r'^useraccounts/', include('useraccounts.urls')),
    url(r'^print/', include('librehatti.prints.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/','librehatti.reports.views.search_form'),
    url(r'^search_result/', SearchResult.as_view()),
    url(r'^save_fields', 'librehatti.reports.views.save_fields'),
    url(r'^list_saved_registers', 'librehatti.reports.views.list_saved_registers'),
    url(r'daily_result', 'librehatti.reports.register.daily_report_result', name='daily_report_result'),
    url(r'^Test_Reports_data/', 'librehatti.Test_Reports.views.Test_Reports_data', name='Test_Reports'),
    url(r'^Reports/', 'librehatti.Test_Reports.views.Reports',name='Reports'),
    url(r'^Soil_building/', 'librehatti.Test_Reports.views.Soil_building_report',name='Soil_building'),
    url(r'^Soil_ohsr/', 'librehatti.Test_Reports.views.Soil_ohsr_report',name='Soil_ohsr'),
    url(r'^Soil_bridge/', 'librehatti.Test_Reports.views.Soil_bridge_report',name='Soil_ohsr'),    
    url(r'consultancy_funds_report', 'librehatti.reports.register.consultancy_funds_report', name='consultancy_funds_report'),    
    url(r'tds_report', 'librehatti.reports.register.tds_report_result', name='tds_report_result'),    
    url(r'payment_report', 'librehatti.reports.register.payment_register', name='payment_register'),
    url(r'suspense_clearance_register', 'librehatti.reports.register.suspense_clearance_register'),
    url(r'servicetax', 'librehatti.reports.register.servicetax_register'),
    url(r'^main_register', 'librehatti.reports.register.main_register', name='main_register'),
    url(r'^proforma_register', 'librehatti.reports.register.proforma_register'),
    url(r'^non_payment_register', 'librehatti.reports.register.non_payment_register'),
    url(r'^client_register', 'librehatti.reports.register.client_register', name='client_register'),
    url(r'^lab_report', 'librehatti.reports.register.lab_report'),
    url(r'^suspense_register', 'librehatti.reports.register.suspense_register'),
    url(r'^tada_form', 'librehatti.reports.register.tada_form'),
    url(r'^tada_register', 'librehatti.reports.register.tada_register'),
    url(r'^tada_staff', 'librehatti.reports.register.tada_staff'),
    url(r'^tadastaffregister', 'librehatti.reports.register.tadastaffregister'),
    url(r'^tada_member', 'librehatti.reports.register.tada_member'),
    url(r'^org_form', 'librehatti.reports.register.org_form'),
    url(r'^org_charges', 'librehatti.reports.register.org_charges'),    
    url(r'^filter_sub_category/', 'librehatti.reports.views.filter_sub_category'),
    url(r'^bill/', 'librehatti.prints.views.bill'),
    url(r'^suspense_bill/', 'librehatti.prints.views.suspense_bill'),
    url(r'^quoted_bill/', 'librehatti.prints.views.quoted_bill'),
    url(r'^tax/', 'librehatti.prints.views.tax'),
    url(r'^bills/', include('librehatti.bills.urls')),
    url(r'^suspense/', include('librehatti.suspense.urls')),
    url(r'^generate_register/', GenerateRegister.as_view(), name='view_register'),
    url(r'^history/','librehatti.reports.previous_history.history'),
    url(r'^details/','librehatti.reports.previous_history.details'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^voucher/', include('librehatti.voucher.urls')),
    url(r'^receipt/', 'librehatti.prints.views.receipt'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^programmeletter/', 'librehatti.programmeletter.views.programmeletter'),
    url(r'^programmerletter_details/', 'librehatti.programmeletter.views.programmerletter_details'),
    url(r'^programmerletter_details/', 'librehatti.programmeletter.views.programmerletter_details'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

