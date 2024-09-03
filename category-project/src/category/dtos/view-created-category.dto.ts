import { ApiProperty } from '@nestjs/swagger';
import { Expose, Type } from 'class-transformer';
import { ViewCategoryDto } from './view-category.dto';

export class ViewCreatedCategoryDto {
  @ApiProperty()
  @Expose()
  id: number;

  @ApiProperty()
  @Expose()
  name: string;

  @ApiProperty()
  @Expose()
  @Type(() => ViewCategoryDto)
  parent: ViewCategoryDto;
}
