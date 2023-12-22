'use client';
import React, {useEffect} from 'react';
import Head from "next/head";
import {transactions} from "@/app/services/transactions";
import {useRouter} from "next/navigation";

type BankOrder = {
    date: string;
    amount: number;
    account_id: number;
};

export default function Page() {
    const [orders, setOrders] = React.useState<BankOrder[]>([]);
    const {push} = useRouter();
    useEffect(() => {
        getOrders();
    }, []);

    const getOrders = async () => {
        const result = await transactions.orders();
        setOrders(result?.data?.data);
    }

    return (
        <>
            <Head>Order</Head>
            <div className="container mx-auto">
                <h1 className="text-3xl font-bold mb-5">Bank Orders</h1>
                <button  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"
                         onClick={() => push('/operations')}
                >
                    Back
                </button>
                <br />
                <br />
                <br />
                <div className="w-full overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-neutral-400">
                    <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Conta</th>
                    </tr>
                    </thead>
                    <tbody className="bg-neutral-700 divide-y divide-gray-200">
                    {orders?.map((order: any, index: number) => (
                        <tr key={index}>
                            <td className="px-6 py-4 whitespace-nowrap">{order.date}</td>
                            <td className="px-6 py-4 whitespace-nowrap">{order.amount}</td>
                            <td className="px-6 py-4 whitespace-nowrap">{order.account_id}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
            </div>
        </>
    );
};

