FROM node:18 as NODE

WORKDIR /vue
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:latest
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=NODE /vue/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
