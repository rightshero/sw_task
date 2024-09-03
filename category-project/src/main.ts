import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(
    new ValidationPipe({
      // adding this whitelist:true ensure that any extra properties in the body will not pass to the controller
      whitelist: true,
    }),
  );
  app.enableCors({
    origin: ['http://localhost:8080'],
    methods: ['POST', 'PUT', 'DELETE', 'GET'],
    allowedHeaders:
      'X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept, Observe, Origin, Authorization',
    credentials: true,
  });
  const config = new DocumentBuilder()
    .setTitle('Unlimited-Subcategories')
    .setDescription('Unlimited-Subcategories API Documentation')
    .setVersion('1.0')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api-docs', app, document);
  await app.listen(process.env.PORT || 3000);
}
bootstrap();
