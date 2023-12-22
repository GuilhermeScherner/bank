import axios from './axiosConfig';

export const transactions = {
    deposit: (params: any): Promise<string> => axios.patch(`/transaction/deposit`, params),
    withdraw: (params: any): Promise<string> => axios.patch(`/transaction/withdraw`, params),
    orders: (): Promise<any> => axios.get(`/transaction/orders`),
}

