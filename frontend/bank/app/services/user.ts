import axios from './axiosConfig';


type Login = {
    username: string;
    password: string;
};



export const user = {
    createUser: (params: any): Promise<any> => axios.post(`/user`, {...params}),
    login: (params: Login): Promise<any> => axios.post(`/user/login`, {...params}),
};

