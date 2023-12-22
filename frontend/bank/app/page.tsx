import Image from 'next/image'

export default function Home() {
    return (
        <div className="bg-gray-100 flex items-center justify-center h-screen">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>
                <form>
                    <div className="mb-4">
                        <label htmlFor="username" className="block text-gray-700 text-sm font-bold mb-2">Username</label>
                        <input type="text" id="username" name="username" className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500" placeholder="Enter your username" required />
                    </div>
                    <div className="mb-6">
                        <label htmlFor="password" className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                        <input type="password" id="password" name="password" className="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500" placeholder="Enter your password" required />
                    </div>
                    <div className="flex items-center justify-between">
                        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue">
                            Login
                        </button>

                        <a href="#" className="text-blue-500 hover:underline">Forgot Password?</a>
                    </div>

                </form>

                <div className="mt-6">
                    <p className="text-sm text-gray-600">Don't have an account?' <a href="#" className="text-blue-500 hover:underline">Sign up</a></p>
                </div>

            </div>

        </div>
    )
}
