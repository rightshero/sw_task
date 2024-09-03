import { ApiProperty } from '@nestjs/swagger';
import { IsInt, IsNotEmpty, IsOptional, IsString, Min } from 'class-validator';

export class CreateCategoryDto {
  @IsString()
  @ApiProperty()
  @IsNotEmpty()
  name: string;

  @IsInt()
  @IsOptional()
  @ApiProperty()
  @Min(1)
  parentId: number;
}
