# Use an official Node.js image
FROM node:18.20-slim

# Install yarn
RUN npm install -g yarn

# Set working directory
WORKDIR /usr/src/app

# Copy package files and install dependencies
COPY package*.json ./
COPY yarn.lock ./
RUN yarn install

# Copy the rest of the application
COPY . .

# Expose port 4567
EXPOSE 4567

# Start the app in development mode
CMD ["yarn", "dev"]