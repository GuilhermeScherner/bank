import {AppProps} from "next/app";

import React from "react";

export default function App({Component, pageProps}: AppProps) {

    return (
        <>
            <div className='min-h-screen flex bg-gray max-h-screen'>
                {/*{isLoading && <LoadingIndicator />}*/}
                {/*{user && pathname !== '/register' && pathname !== '/login' && (*/}
                {/*    <AppLayout />*/}
                {/*)}*/}
                {/*{authorized && <Component {...pageProps} />}*/}
                <Component {...pageProps} />
            </div>
        </>

    );

}

