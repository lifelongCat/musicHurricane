FROM node:22.2.0

WORKDIR /frontend

# install node dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# copy project files
COPY . .

# run app
CMD ["npm", "start"]
