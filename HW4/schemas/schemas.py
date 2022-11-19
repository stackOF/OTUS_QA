from pydantic import BaseModel


class DogApi(BaseModel):
    message: list
    status: str


class BreweryApi(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: str = None
    address_2: str = None
    address_3: str = None
    city: str = None
    state: str = None
    county_province: str = None
    postal_code: str = None
    country: str = None
    longitude: str = None
    latitude: str = None
    phone: str = None
    website_url: str = None
    updated_at: str
    created_at: str


class JsonPlaceholderApiComments(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class JsonPlaceholderApiPosts(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class JsonPlaceholderApiAlbums(BaseModel):
    userId: int
    id: int
    title: str


class JsonPlaceholderApiPhotos(BaseModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str


class JsonPlaceholderApiTodos(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
