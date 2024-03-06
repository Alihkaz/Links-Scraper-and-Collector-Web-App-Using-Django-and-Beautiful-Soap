from django.contrib import admin


from .models import Link


#customasing the admin panel :

admin.site.site_header="Link Extractor"

admin.site.site_title="Link Extractor"

admin.site.index_title="Manage Your App"


admin.site.register(Link)
