import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { IsNull, Repository } from 'typeorm';
import { Category } from './entities/category.entity';
import { CreateCategoryDto } from './dtos/create-category.dto';

@Injectable()
export class CategoryService {
  constructor(
    @InjectRepository(Category)
    private categoryRepository: Repository<Category>,
  ) {}

  async createCategory(body: CreateCategoryDto): Promise<Category> {
    const { name, parentId } = body;
    const parent = parentId
      ? await this.categoryRepository.findOne({
          where: { id: parentId },
        })
      : null;

    if (parentId && !parent) {
      throw new NotFoundException('Parent category not found');
    }
    const category = this.categoryRepository.create({ name, parent });
    return this.categoryRepository.save(category);
  }

  async findAll(): Promise<Category[]> {
    return this.categoryRepository.find({ relations: ['subcategories'] });
  }

  async findMain(): Promise<Category[]> {
    return this.categoryRepository.find({
      where: { parent: IsNull() },
    });
  }

  async findSubcategories(parentId: number): Promise<Category[]> {
    const parent = await this.categoryRepository.findOne({
      where: { id: parentId },
    });
    if (!parent) {
      throw new NotFoundException('Parent category not found');
    }
    const subcategories = await this.categoryRepository.find({
      where: { parent: parent },
    });
    if (subcategories.length === 0) {
      // Create 2 subcategories
      const categoryName = parent.name;
      const subcategoryA = this.categoryRepository.create({
        name: `SUB ${categoryName}-1`,
        parent,
      });
      const subcategoryB = this.categoryRepository.create({
        name: `SUB ${categoryName}-2`,
        parent,
      });
      const subA = await this.categoryRepository.save(subcategoryA);
      const subB = await this.categoryRepository.save(subcategoryB);
      return [subA, subB];
    } else {
      return subcategories;
    }
  }
}
