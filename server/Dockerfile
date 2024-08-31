FROM  node:14

#creating app directoryy
WORKDIR /app 

#copying package file (package and package-lock)
COPY package*.json ./

RUN npm install

#bundle app source
COPY . .

EXPOSE 5000

CMD ["npm", "start" ]