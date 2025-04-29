export abstract class BaseRepository<T> {
    protected items: T[] = [];

    public abstract find(id: number): T | undefined;

    public abstract findAll(): T[];

    public abstract create(item: T): void;

    public abstract update(id: number, item: T): void;

    public abstract delete(id: number): void;
}