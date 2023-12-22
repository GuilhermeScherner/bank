import { isAuthenticated } from '@/lib/auth';

// export async function getServerSideProps(context: any) {
//     if (!isAuthenticated()) {
//         return {
//             redirect: {
//                 destination: '/login',
//                 permanent: false,
//             },
//         };
//     }
//
//     // Fetch data for authenticated user here
//     const data = await fetchUserData();
//
//     return {
//         props: {
//             data,
//         },
//     };
// }


// export async function getServerSideProps(context) {
//     if (isAuthenticated()) {
//         return {
//             redirect: {
//                 destination: '/',
//                 permanent: false,
//             },
//         };
//     }
//
//     return {
//         props: {},
//     };
// }