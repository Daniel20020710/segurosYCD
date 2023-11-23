
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('Apps.personas.urls')),
      path('accidentes/', include('Apps.accidentes.urls')),
        path('vehiculos/', include('Apps.vehiculos.urls')),
          path('multas/', include('Apps.multas.urls')),
            path('involucrar/', include('Apps.involucrar.urls')),
              path('aplicarMultas/', include('Apps.aplicar_multas.urls')),
                path('propietarios/', include('Apps.propietarios.urls')),
                 

]
 