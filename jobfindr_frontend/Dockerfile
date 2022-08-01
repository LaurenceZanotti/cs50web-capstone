FROM node:lts
COPY . /usr/src/app_front
WORKDIR /usr/src/app_front
RUN npm install
EXPOSE 3000
CMD ["npx", "next", "dev"]