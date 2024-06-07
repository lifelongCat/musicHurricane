import axios from "axios";

export default class CompositionService {
    static async getAll() {
        return await axios.get(`http://localhost:${process.env.REACT_APP_DJANGO_PORT}/api/compositions/`);
    }
}
