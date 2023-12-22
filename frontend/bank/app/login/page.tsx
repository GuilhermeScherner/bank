'use client';
import React, {useState} from "react";
import Head from 'next/head';
import {user} from "@/app/services/user";
import {FormProvider, SubmitHandler, useForm} from "react-hook-form";

import {useRouter} from "next/navigation";

export type LoginFormInputs = {
    password: string;
    username: string;
};
export default function Page() {
    const {push} = useRouter();

    const onSubmit = async (data: any) => {
        try {
            const {username, password} = data;
            const result = await user.login({username, password});
            localStorage.setItem('token', result?.data?.token);
            push('/operations');
        } catch (e) {
            console.log(e)
        }
    };

    const {
        handleSubmit,
        setValue,
        register,
        formState: {errors},
    } = useForm<LoginFormInputs>({});

    return (
        <>
            <Head>Login</Head>
            <div className="bg-gray-100 flex items-center justify-center h-screen">
                <div className="bg-blend-darken p-8 rounded shadow-md w-96">
                    <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>
                    <form onSubmit={handleSubmit((data) => onSubmit(data))}>
                            <div className="mb-4">
                                <label htmlFor="username"
                                       className="block text-gray-700 text-sm font-bold mb-2">Username</label>
                                <input {...register("username")}
                                    type="text" id="username" name="username"
                                       className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                                       placeholder="Enter your username" required/>

                            </div>
                            <div className="mb-6">
                                <label htmlFor="password"
                                       className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                                <input {...register("password")}
                                    type="password" id="password" name="password"
                                       className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                                       placeholder="Enter your password" required/>
                            </div>
                            <div className="flex items-center justify-between">
                                <button type="submit"
                                        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue">
                                    Login
                                </button>

                                <a href="#" className="text-blue-500 hover:underline">Forgot Password?</a>
                            </div>
                        </form>
                    <div className="mt-6">
                        <p className="text-sm text-gray-600">Do not have an account<a href="#"
                                                                                      className="text-blue-500 hover:underline">Sign
                            up</a></p>
                    </div>
                </div>
            </div>
        </>
    )
}
