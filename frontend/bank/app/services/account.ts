import axios from './axiosConfig';


export const account = {
    balance: (): Promise<any> => axios.get(`/account/balance`),
    block: (): Promise<any> => axios.get(`/account/block`),
    unblock: (): Promise<any> => axios.get(`/account/unblock`),
}
