import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Assignment, AssignmentDocument } from '../schema/assignment.schema';

@Injectable()
export class AssignmentService {
  constructor(
    @InjectModel(Assignment.name)
    private assignmentModel: Model<AssignmentDocument>,
  ) {}

  async getAssignmentAll(): Promise<Assignment[]> {
    return this.assignmentModel.find().exec();
  }

  async getAssignmentById(id: number): Promise<Assignment[]> {
    return this.assignmentModel.find({ id: id }).exec();
  }

  async getAssignmentBySubjectName(name: string): Promise<Assignment[]> {
    return this.assignmentModel.find({ subject: name.toUpperCase() }).exec();
  }

  async getAssignmentBySubjectNameAndCount(
    name: string,
    count: number,
  ): Promise<Assignment[]> {
    return this.assignmentModel
      .find({ subject: name.toUpperCase(), count: count })
      .exec();
  }

  async getAssignmentByMonth(count: number): Promise<Assignment[]> {
    return this.assignmentModel.find({ month: count }).exec();
  }

  async getAssignmentByWeek(count: number): Promise<Assignment[]> {
    return this.assignmentModel.find({ week: count }).exec();
  }
}
