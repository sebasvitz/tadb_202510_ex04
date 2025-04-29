export class Entity {
    id: number;
    createdAt: Date;
    updatedAt: Date;

    constructor(id: number) {
        this.id = id;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }
}