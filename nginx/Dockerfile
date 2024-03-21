# Použití oficiálního NGINX image
FROM nginx:latest

# Použití pracovního adresáře /app Sem se kopírují soubory
WORKDIR /app

# Kopírování vlastního konfiguračního souboru
COPY nginx.conf /etc/nginx/nginx.conf
COPY start-nginx.sh /start-nginx.sh
RUN chmod +x /start-nginx.sh

# Kopírování static souborů do adresáře /app
COPY ./static ./static

# Nastavení oprávnění na static soubory pro uživatele nginx
RUN chown -R nginx:nginx /app/static