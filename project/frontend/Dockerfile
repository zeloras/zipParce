FROM node:14.16.1-alpine3.10

WORKDIR /usr/app

COPY package.json .
RUN npm install --quiet

COPY . .

CMD ["npm", "run", "serve"]