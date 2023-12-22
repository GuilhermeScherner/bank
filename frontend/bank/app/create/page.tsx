'use client';
import Head from "next/head";
import React from 'react';
import { useForm} from 'react-hook-form';
import { Label } from '@/components/label';
import { Button } from '@/components/button';
import {user} from "@/app/services/user";
import {useRouter} from "next/navigation";
export type CreateFormInputs = {
    name: string;
    username: string;
    cpf: string;
    birth_date: Date;
    password: string;
};
export default function Page() {
    const {
        handleSubmit,
        setValue,
        register,
        formState: {errors},
        reset
    } = useForm<CreateFormInputs>({});
    const {push} = useRouter();
    const onSubmit = async (data: any) => {
        try{
            await user.createUser(data);
            reset();
        }catch (e) {
            console.log(e)
        }
    };

    return (
        <>
        <Head>Create</Head>
        <div className="container mx-auto justify-center">
            <h1 className="text-3xl font-bold mb-5">Bank Orders</h1>
            <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg"
                onClick={() => push('/operations')}
            >
                Check Orders
            </button>
            <br />
            <br />
            <div className="w-1/2 p-5 bg-white rounded-lg shadow-lg">s
                <form onSubmit={handleSubmit((data) => onSubmit(data))}>
                <Label>Name</Label>
                    <input {...register("name")}
                           type="text" id="name" name="name"
                           className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                           placeholder="Enter your name" required/>

                <Label>Username</Label>
                    <input {...register("username")}
                           type="text" id="username" name="username"
                           className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                           placeholder="Enter your username" required/>
                <Label>CPF</Label>
                    <input {...register("cpf")}
                           type="text" id="cpf" name="cpf"
                           className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                           placeholder="Enter your cpf" required/>

                <Label>Birth Date</Label>
                    <input {...register("birth_date")}
                           type="date" id="birth_date" name="birth_date"
                           className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                           placeholder="Enter your birth date" required/>

                <Label>Password</Label>
                    <input {...register("password")}
                           type="password" id="password" name="password"
                           className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500 bg-neutral-700"
                           placeholder="Enter your password" required/>

                <Button type="submit">Create User</Button>
            </form>
            </div>
        </div>
        </>

    );
};
