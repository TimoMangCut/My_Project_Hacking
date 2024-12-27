FROM php:8.1-apache
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    && apt-get install -y libxml2-dev \
    && docker-php-ext-install pdo pdo_pgsql pgsql
RUN a2enmod rewrite
COPY . /var/www/html/
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80
CMD ["apache2-foreground"]