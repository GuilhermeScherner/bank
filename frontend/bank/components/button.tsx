import React from 'react';
import { motion } from 'framer-motion';

const inputVariants = {
    hidden: { scale: 0.8, opacity: 0 },
    visible: { scale: 1, opacity: 1 },
};

type ButtonProps = {
    children: React.ReactNode;
    type:  "submit" | "reset" | "button" | undefined;
};



export const Button = ({ children, type }: ButtonProps) => {
    return (
        <motion.button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            type={type}
            initial="hidden"
            animate="visible"
            transition={{ delay: 0.3 }}
            variants={inputVariants}
        >
            {children}
        </motion.button>
    );
};

