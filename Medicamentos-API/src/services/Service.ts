class Service {
    constructor(private repository: BaseRepository) {}

    async find(id: number) {
        return await this.repository.find(id);
    }

    async findAll() {
        return await this.repository.findAll();
    }

    async create(entity: Entity) {
        return await this.repository.create(entity);
    }

    async update(id: number, entity: Entity) {
        return await this.repository.update(id, entity);
    }

    async delete(id: number) {
        return await this.repository.delete(id);
    }
}