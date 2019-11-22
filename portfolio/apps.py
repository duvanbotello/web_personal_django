from django.apps import AppConfig

# lo que hago es cambiar el nombre de como se muestra en el admin de portafolio
class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = 'Portafolio'
