import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import * as z from 'zod';
import { apiClient } from '../../lib/api-client';
import {CONFIG} from '../../core/config';

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

                <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-6 items-center'>
                    <div>
                        <h1 className='text-base/7 font-semibold relative'>Login</h1>
                        <p className='mt-1 text-sm/6 text-gray-800'>Enter your ERP credentials to login to your account</p>
                    </div>
                    <div className='items-center'>
                        <label htmlFor='username' className='block text-sm/6 font-medium'>Username</label>
                        <input
                        {...register('username')}
                        className='border rounded-md text-sm/7 mt-2'
                        type='text'
                        name='username'
                        id='username'
                        placeholder='email@example.com'
                        />
                        {errors.username && <p>{errors.username.message}</p>}
                    </div>
                    <div>
                        <label className='block text-sm/6 font-medium'>Password</label>
                        <input
                        type='password'
                        {...register('password')}
                        className='border rounded-md text-sm/7 placeholder: center'
                        name='password'
                        id='password'
                        placeholder='***'
                        />
                        {errors.password && <p>{errors.password.message}</p>}
                    </div>

                    <button
                    disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Authenticating' : 'Sign In'}
                    </button>
                </form>
            </div>
        </div>
    );
}}