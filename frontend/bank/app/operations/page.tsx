'use client';
import React, {useEffect, useState} from 'react';
import Head from "next/head";
import {transactions} from "@/app/services/transactions";
import {account} from "@/app/services/account";
import {useRouter} from "next/navigation";

export default function Page() {
    const [depositAmount, setDepositAmount] = useState(0);
    const [withdrawAmount, setWithdrawAmount] = useState(0);
    const [balance, setBalance] = useState(0);
    const {push} = useRouter();
    const handleDeposit = async () => {
        try {
            await transactions.deposit({amount: depositAmount})
            getBalance();
        }catch (e) {
            console.log(e)
        }
    };

    const handleWithdraw = async () => {
        try {
            console.log(withdrawAmount)
            await transactions.withdraw({amount: withdrawAmount});
            getBalance();
        }catch (e) {
            console.log(e)
        }
    };

    useEffect(() => {
        getBalance();
    }, []);

    async function getBalance() {
        const result = await account.balance();
        setBalance(result?.data?.balance)
    }


    return (
        <>
            <Head>Operations</Head>
            <div className="container mx-auto">
                <h1 className="text-3xl font-bold mb-5">Bank Orders</h1>
                <div className="mt-10 text-center">
                    <h2 className="text-2xl font-bold mb-5">Your Balance</h2>
                    <p className="text-5xl font-bold">${balance || 0}</p>
                </div>
                <br />
                <br />
                <div className="flex justify-center">
                    <div className="w-1/2 p-5 bg-white rounded-lg shadow-lg">
                        <h2 className="text-xl font-bold mb-5 text-black">Make a deposit</h2>
                        <input
                            type="number"
                            className="border-2 border-gray-300 p-2 rounded-lg w-full mb-5 bg-neutral-700"
                            placeholder="Enter amount"
                            value={depositAmount}
                            onChange={(e) => setDepositAmount(parseInt(e.target.value))}
                        />
                        <button
                            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"
                            onClick={handleDeposit}
                        >
                            Deposit
                        </button>
                    </div>
                    <div className="w-1/2 p-5 bg-white rounded-lg shadow-lg">
                        <h2 className="text-xl font-bold mb-5 text-black">Make a withdraw</h2>
                        <input
                            type="number"
                            className="border-2 border-gray-300 p-2 rounded-lg w-full mb-5 bg-neutral-700"
                            placeholder="Enter amount"
                            value={withdrawAmount}
                            onChange={(e) => setWithdrawAmount(parseInt(e.target.value))}
                        />
                        <button
                            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg"
                            onClick={handleWithdraw}
                        >
                            Withdraw
                        </button>
                    </div>
                </div>
                <br />
                <br />
                <div className="flex justify-between">
                    <button
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"
                        onClick={() => push('/orders')}
                    >
                        Check Orders
                    </button>

                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"
                            onClick={() => push('/create')}
                    >
                        Criar conta
                    </button>
                </div>

            </div>
        </>
    );
};

