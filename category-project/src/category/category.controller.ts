import {
  Controller,
  Post,
  Body,
  Get,
  Param,
  ParseIntPipe,
  Query,
} from '@nestjs/common';
import { CategoryService } from './category.service';
import { Category } from './entities/category.entity';
import { CreateCategoryDto } from './dtos/create-category.dto';
import {
  ApiBadRequestResponse,
  ApiCreatedResponse,
  ApiInternalServerErrorResponse,
  ApiNotFoundResponse,
  ApiOkResponse,
  ApiOperation,
  ApiParam,
  ApiQuery,
  ApiTags,
} from '@nestjs/swagger';
import { ViewCreatedCategoryDto } from './dtos/view-created-category.dto';

@Controller('categories')
@ApiTags('categories')
export class CategoryController {
  constructor(private readonly categoryService: CategoryService) {}

  @Post('initialize')
  async initializeCategories(): Promise<Category[]> {
    const existingCategories = await this.categoryService.findMain();
    if (existingCategories.length > 0) {
      return existingCategories;
    }

    const categoryA = await this.categoryService.createCategory({
      name: 'Category A',
      parentId: null,
    });
    const categoryB = await this.categoryService.createCategory({
      name: 'Category B',
      parentId: null,
    });
    return [categoryA, categoryB];
  }

  @Post()
  @ApiCreatedResponse({ type: ViewCreatedCategoryDto })
  @ApiBadRequestResponse({ description: 'Bad Request' })
  @ApiNotFoundResponse({ description: 'Category not found' })
  @ApiInternalServerErrorResponse({ description: 'Internal server error' })
  @ApiOperation({ summary: 'Used to create a category' })
  createCategory(@Body() body: CreateCategoryDto): Promise<Category> {
    return this.categoryService.createCategory(body);
  }

  @Get(':parentId/subcategories')
  @ApiParam({
    name: 'parentId',
    required: true,
    description: 'the id of the parent category',
    type: 'number',
  })
  @ApiOkResponse({ type: ViewCreatedCategoryDto, isArray: true })
  @ApiBadRequestResponse({ description: 'Bad Request' })
  @ApiNotFoundResponse({ description: 'Category not found' })
  @ApiInternalServerErrorResponse({ description: 'Internal server error' })
  @ApiOperation({ summary: 'Used to get subcategories of a category' })
  async findSubcategories(
    @Param('parentId', ParseIntPipe) parentId: number,
  ): Promise<Category[]> {
    return this.categoryService.findSubcategories(parentId);
  }

  @Get()
  @ApiBadRequestResponse({ description: 'Bad Request' })
  @ApiInternalServerErrorResponse({ description: 'Internal server error' })
  @ApiOperation({ summary: 'Used to get all the categories' })
  @ApiOkResponse({ type: ViewCreatedCategoryDto, isArray: true })
  findAll(): Promise<Category[]> {
    return this.categoryService.findAll();
  }
}
