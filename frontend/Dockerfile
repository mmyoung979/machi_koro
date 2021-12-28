# Build the application
from node:14.18.1 as build
WORKDIR /usr/src
COPY package.json /usr/src
RUN npm install
COPY . /usr/src
RUN npm run-script build

# Copy artifacts to the server
FROM nginx
COPY --from=build /usr/src/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]