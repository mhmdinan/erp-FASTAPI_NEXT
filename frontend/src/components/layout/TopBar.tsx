import { useNavigate, Link } from 'react-router-dom';

export default function TopBar() {
    const navigate = useNavigate();

    const handleLogout = () =>  {
        localStorage.removeItem('token');

        navigate('/login', {replace: true});
    };

    return (
        <header className='bg-indigo-800 h-16 border-b sticky justify-between flex px-6 py-3'>
            <div className='gap-6'>
                <Link
                to='dashboard'
                className='w-fit rounded-md px-3 py-1 flex items-center gap-2 border border-transparent bg-blue-600 hover:bg-blue-800 transition-all duration-200'
                title='Go to Dashboard'
                >
                <span className='text-white font-semibold'>
                    Home
                </span>
                </Link>
            </div>

            <div className='gap-6'>
                <button
                onClick={handleLogout}
                className='gap-2 bg-red-500 border border-transparent rounded-md px-3 py-1 shadow-md hover:bg-red-800 transition-all duration-200 border-red-900/50 active:scale-95'
                >
                    <span className='text-white font-semibold text-sm'>
                        Logout
                    </span>
                </button>
            </div>
        </header>
    )
}