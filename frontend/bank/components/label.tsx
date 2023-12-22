import React from 'react';
import { motion } from 'framer-motion';

const inputVariants = {
    hidden: { scale: 0.8, opacity: 0 },
    visible: { scale: 1, opacity: 1 },
};

type LabelProps = {
    children: React.ReactNode;
};

export const Label = ({ children }: LabelProps) => {
    return (
        <motion.label
            className="block text-gray-700 text-sm font-bold mb-2"
    initial="hidden"
    animate="visible"
    transition={{ delay: 0.3 }}
    variants={inputVariants}
        >
        {children}
        </motion.label>
);
};

