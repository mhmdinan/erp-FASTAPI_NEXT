import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import * as z from 'zod';
import { apiClient } from '../../lib/api-client';

const loginSchema = z.object({
    username: z.string().min(1, "username is required"),
    password: z.string().min(6, "Password must atleast be 6 characters"),
});

type loginFormValues = z.infer<typeof loginSchema>;

export default function LoginPage() {{
    const navigate = useNavigate();
    const {register, handleSubmit, formState: {errors, isSubmitting}} = useForm<loginFormValues>({
        resolver: zodResolver(loginSchema),
    });

    const onSubmit = async (data: loginFormValues) => {
        try {
            const formData = new FormData();
            formData.append('username', data.username);
            formData.append('password', data.password);

            const response = await apiClient.post('/auth/login', formData);

            localStorage.setItem('token', response.data.access_token);

            navigate('/dashboard');
        } catch (error) {
            alert("Invalid credentials. Please check your FastAPI console");
        }
    };

    return (
        <div className='flex min-h-screen items-center justify-center'>
            <div>

                <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-6 items-center justify-center'>
                    <div className='flex flex-col justify-center'>
                        <h1 className='text-base/7 font-semibold text-center'>Login</h1>
                        <p className='mt-1 text-sm/6 text-gray-800 text-center'>Enter your credentials to login to your account</p>
                    </div>
                    <div className='relative'>
                        <label htmlFor='username' className='block text-sm/6 font-medium'>Username</label>
                        <input
                        {...register('username')}
                        className='border rounded-md text-sm/7 mt-2 px-3'
                        type='text'
                        name='username'
                        id='username'
                        placeholder='email@example.com'
                        />
                        {errors.username && <p className='text-red-500 text-xs h-5'>{errors.username.message}</p>}
                    </div>
                    <div>
                        <label className='block text-sm/6 font-medium'>Password</label>
                        <input
                        type='password'
                        {...register('password')}
                        className='border rounded-lg text-sm/7 px-3'
                        name='password'
                        id='password'
                        placeholder='******'
                        />
                        {errors.password && <p className='text-red-500 text-xs h-5'>{errors.password.message}</p>}
                    </div>

                    <button
                    className='bg-indigo-500 text-white border rounded-md px-3 py-1 font-semibold shadow-md hover:bg-indigo-800 transition duration-200 active:scale-95'
                    disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Authenticating' : 'Sign In'}
                    </button>
                </form>
            </div>
        </div>
    );
}}