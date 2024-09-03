import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CategoryModule } from './category/category.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { Category } from './category/entities/category.entity';

@Module({
  imports: [
    CategoryModule,
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath:
        process.env.NODE_ENV === 'development' ? `.env.development` : '.env',
    }),
    TypeOrmModule.forRootAsync({
      inject: [ConfigService],
      useFactory: (config: ConfigService) => {
        if (process.env.NODE_ENV === 'development') {
          return {
            type: 'postgres',
            ssl: process.env.NODE_ENV === 'development' ? false : true,
            host: config.getOrThrow<string>('DATABASE_HOST'),
            port: config.getOrThrow<number>('DATABASE_PORT'),
            database: config.getOrThrow<string>('DATABASE_NAME'),
            username: config.getOrThrow<string>('DATABASE_USER'),
            password: config.getOrThrow<string>('DATABASE_PASSWORD'),
            entities: [Category],
            logger: 'file',
            logging: false,
            synchronize: true,
          };
        } else {
          return {
            type: 'postgres',
            ssl: process.env.NODE_ENV === 'development' ? false : true,
            host: config.getOrThrow<string>('DATABASE_HOST'),
            port: config.getOrThrow<number>('DATABASE_PORT'),
            database: config.getOrThrow<string>('DATABASE_NAME'),
            username: config.getOrThrow<string>('DATABASE_USER'),
            password: config.getOrThrow<string>('DATABASE_PASSWORD'),
            entities: [Category],
            logger: 'file',
            logging: false,
            synchronize: true,
          };
        }
      },
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
